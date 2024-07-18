import math
import cadquery as cq

frames = {
    250: (370, 370), # X, Y Inside length of frame
    300: (420, 420),
    350: (470, 470)
}

tool_count      = 6     # Number of tools (No more than 6)
frame_size      = 300   # Choose frame from frames dict
th_board_offset = 60    # Y offset from inside of the frame to tool PCB while docked
calc_centers    = True  # If true, umbilical plate and dock centers will be spaced evenly
dock_centers    = 60    # Distance between dock centers (ignored if calc_centers is True)
back_centers    = 23.5  # Umbilical plate centers by tool count
length          = 12.5  # Nominal sickout from umbilical plate
angle           = 56.5  # Umbilical socket angle
depth           = 13    # Umbilical socket inner depth
fillet_size     = 2     # Umbilical socket to plate fillet size (zero to disable)


if calc_centers and tool_count > 1:
    # back_centers = 118 / (tool_count-1)
    dock_centers = (frames[frame_size][0]-60) / (tool_count-1)

tool_vars = {
    0: [
        {"back_offset": 0, "dock_offset": 0} # 0
    ],
    1: [
        {"back_offset": -back_centers/2, "dock_offset": -dock_centers/2}, # 0
        {"back_offset": back_centers/2, "dock_offset": dock_centers/2}    # 1
    ],
    2: [
        {"back_offset": -back_centers, "dock_offset": -dock_centers}, # 0
        {"back_offset": 0, "dock_offset": 0},                         # 1
        {"back_offset": back_centers, "dock_offset": dock_centers},   # 2

    ],
    3: [
        {"back_offset": -((back_centers/2)+back_centers), "dock_offset": -((dock_centers/2)+dock_centers)}, # 0
        {"back_offset": -back_centers/2, "dock_offset": -dock_centers/2},                                   # 1
        {"back_offset":  back_centers/2, "dock_offset":  dock_centers/2},                                   # 2
        {"back_offset": ((back_centers/2)+back_centers), "dock_offset": ((dock_centers/2)+dock_centers)},   # 3

    ],
    4: [
        {"back_offset": -back_centers*2, "dock_offset": -dock_centers*2}, # 0
        {"back_offset": -back_centers, "dock_offset": -dock_centers},     # 1
        {"back_offset": 0, "dock_offset": 0},                             # 2
        {"back_offset": back_centers, "dock_offset": dock_centers},       # 3
        {"back_offset": back_centers*2, "dock_offset": dock_centers*2},   # 4

    ],
    5: [
        {"back_offset": -((back_centers/2)+(back_centers*2)), "dock_offset": -((dock_centers/2)+(dock_centers*2))}, # 0
        {"back_offset": -((back_centers/2)+back_centers), "dock_offset": -((dock_centers/2)+dock_centers)},         # 1
        {"back_offset": -back_centers/2, "dock_offset": -dock_centers/2},                                           # 2
        {"back_offset":  back_centers/2, "dock_offset":  dock_centers/2},                                           # 3
        {"back_offset": ((back_centers/2)+back_centers), "dock_offset": ((dock_centers/2)+dock_centers)},           # 4
        {"back_offset": (back_centers/2)+(back_centers*2), "dock_offset": (dock_centers/2)+(dock_centers*2)},       # 5
    ],
}

blank    = cq.importers.importStep("umbilical_blank.step")
negative = cq.Workplane().box(160, 100, 150).translate((0, 50, 0)).cut(blank)
plate    = cq.Workplane().box(160, 10, 150).translate((0, 5, 0))

sk = (
    cq.Sketch()
    .arc((3, 0), 6.5, 0, 360)
    .arc((-3, 0), 6.5, 0, 360)
    .arc((0, 3), 5, 0, 360)
    .hull()
)

sk_inner = (
    cq.Sketch()
    .arc((3, 0), 7.3/2, 0, 360)
    .arc((-3, 0), 7.3/2, 0, 360)
    .arc((0, 3), 4.3/2, 0, 360)
    .hull()
)

sk_inner2 = (
    cq.Sketch()
    .arc((3, 0), 6.3/2, 0, 360)
    .arc((-3, 0), 6.3/2, 0, 360)
    .arc((0, 3), 3.3/2, 0, 360)
    .hull()
)

tool_shape = (
    cq.Workplane().placeSketch(sk).extrude(length*4).translate((0, 0, -length*3))
    .faces(">Z").workplane().placeSketch(sk_inner).cutBlind(-depth)
    .faces(">Z").workplane().placeSketch(sk_inner2).cutBlind(-length*4)

    .faces(">Z").edges().item(0).fillet(1.5)
    .faces(">Z").edges().item(6).chamfer(0.3, 3)
)

for tool in range(tool_count):
    back_offset = tool_vars[tool_count-1][tool]['back_offset']
    dock_offset = tool_vars[tool_count-1][tool]['dock_offset']
    dock_angle  = math.atan((dock_offset-back_offset)/(frames[frame_size][1] + 20 - th_board_offset)) * 180 / math.pi

    if tool <= tool/2:
        dock_angle  = -abs(dock_angle)
        back_offset = -abs(back_offset)

    inner = (
        cq.Workplane().placeSketch(sk_inner).extrude(length*4).translate((0, 0, -length*2))
        .rotate((0, 0, 0), (1, 0, 0), angle)
        .rotate((0, 0, 0), (0, 0, 1), dock_angle)
        .translate((back_offset, 0, 0))
    )

    body = (
        tool_shape
        .rotate((0, 0, 0), (1, 0, 0), angle)
        .rotate((0, 0, 0), (0, 0, 1), dock_angle)
        .translate((back_offset, 0, 0))
    )

    plate = plate.cut(inner)
    plate = plate.union(body)


if fillet_size > 0:
    try:
        plate = plate.faces(cq.NearestToPointSelector((0, 0, 0))).edges().fillet(fillet_size)
    except:
        print("Failed to apply fillet(s)")

result = plate.cut(negative).rotate((0, 0, 0), (1, 0, 0), -90)


try:
    show_object(result)

except NameError:
    cq.exporters.export(result, f"UMB_plate_{tool_count}_tool_{frame_size}mm.step")
    cq.exporters.export(result, f"UMB_plate_{tool_count}_tool_{frame_size}mm.stl")

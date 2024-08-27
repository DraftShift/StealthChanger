import math
import cadquery as cq

frames = {
    250: (370, 370), # X, Y Inside length of frame
    300: (420, 420),
    350: (470, 470)
}

frames = {
    250: (370, 370, 5), # X, Y Inside length of frame, MAX tool count
    300: (420, 420, 6),
    350: (470, 470, 6)
}

tool_count      = 2     # Number of tools (No more than 6)
frame_size      = 300   # Choose frame from frames dict
th_board_offset = 60    # Y offset from inside of the frame to tool PCB while docked
calc_centers    = True  # If true, dock centers will be spaced evenly
dock_centers    = 60    # Distance between dock centers (ignored if calc_centers is True)
back_centers    = [0, 23.5, 24, 23.5, 23.5, 23.5, 23.5] # Umbilical plate centers by tool count
length          = 12.5  # Nominal sickout from umbilical plate
angle           = 56.5  # Umbilical socket angle
depth           = 13    # Umbilical socket inner depth
fillet_size     = 2     # Umbilical socket to plate fillet size (zero to disable)


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



def backPlate(printer_size=300, tool_count=6):
    blank    = cq.importers.importStep("umbilical_blank.step")
    negative = cq.Workplane().box(160, 100, 150).translate((0, 50, 0)).cut(blank)
    plate    = cq.Workplane().box(160, 10, 150).translate((0, 5, 0))

    if calc_centers and tool_count > 1:
        dock_centers = (frames[printer_size][0]-60) / (tool_count-1)
    else:
        dock_centers = 0

    tool_vars = {
        0: [
            {"back_offset": 0, "dock_offset": 0} # 0
        ],
        1: [
            {"back_offset": -back_centers[tool_count]/2, "dock_offset": -dock_centers/2}, # 0
            {"back_offset": back_centers[tool_count]/2, "dock_offset": dock_centers/2}    # 1
        ],
        2: [
            {"back_offset": -back_centers[tool_count], "dock_offset": -dock_centers}, # 0
            {"back_offset": 0, "dock_offset": 0},                                     # 1
            {"back_offset": back_centers[tool_count], "dock_offset": dock_centers},   # 2

        ],
        3: [
            {"back_offset": -((back_centers[tool_count]/2)+back_centers[tool_count]), "dock_offset": -((dock_centers/2)+dock_centers)}, # 0
            {"back_offset": -back_centers[tool_count]/2, "dock_offset": -dock_centers/2},                                               # 1
            {"back_offset":  back_centers[tool_count]/2, "dock_offset":  dock_centers/2},                                               # 2
            {"back_offset": ((back_centers[tool_count]/2)+back_centers[tool_count]), "dock_offset": ((dock_centers/2)+dock_centers)},   # 3

        ],
        4: [
            {"back_offset": -back_centers[tool_count]*2, "dock_offset": -dock_centers*2}, # 0
            {"back_offset": -back_centers[tool_count], "dock_offset": -dock_centers},     # 1
            {"back_offset": 0, "dock_offset": 0},                                         # 2
            {"back_offset": back_centers[tool_count], "dock_offset": dock_centers},       # 3
            {"back_offset": back_centers[tool_count]*2, "dock_offset": dock_centers*2},   # 4

        ],
        5: [
            {"back_offset": -((back_centers[tool_count]/2)+(back_centers[tool_count]*2)), "dock_offset": -((dock_centers/2)+(dock_centers*2))}, # 0
            {"back_offset": -((back_centers[tool_count]/2)+back_centers[tool_count]), "dock_offset": -((dock_centers/2)+dock_centers)},         # 1
            {"back_offset": -back_centers[tool_count]/2, "dock_offset": -dock_centers/2},                                                       # 2
            {"back_offset":  back_centers[tool_count]/2, "dock_offset":  dock_centers/2},                                                       # 3
            {"back_offset": ((back_centers[tool_count]/2)+back_centers[tool_count]), "dock_offset": ((dock_centers/2)+dock_centers)},           # 4
            {"back_offset": (back_centers[tool_count]/2)+(back_centers[tool_count]*2), "dock_offset": (dock_centers/2)+(dock_centers*2)},       # 5
        ],
    }

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

    return result

try:
    show_object(backPlate(printer_size=frame_size, tool_count=tool_count))

except NameError:
    # if run via commandline export for release
    import os
    current_path = os.getcwd()
    stl_path     = os.path.join(current_path, "STL")
    step_path    = os.path.join(current_path, "STEP")
    stl_regular  = os.path.join(stl_path,  "Regular")
    step_regular = os.path.join(step_path, "Regular")

    for x in [stl_path, step_path, stl_regular, step_regular]:
        if not os.path.exists(x):
            os.makedirs(x)

    # Single tool
    name = "Regular_1_tool"
    print("Generating", name)

    step = os.path.join(step_regular, f"{name}.step")
    cq.exporters.export(backPlate(tool_count=1), step)

    stl = os.path.join(stl_regular, f"{name}.stl")
    cq.exporters.export(backPlate(tool_count=1), stl, angularTolerance=0.3)

    # Multi Tool
    for printer_size in frames:
        max_tool_count = frames[printer_size][2]

        for tool_count in range(2, max_tool_count+1):
            step_size_path = os.path.join(step_regular, str(printer_size))

            if not os.path.exists(step_size_path):
                os.makedirs(step_size_path)

            stl_size_path = os.path.join(stl_regular, str(printer_size))

            if not os.path.exists(stl_size_path):
                os.makedirs(stl_size_path)

            name = f"Regular_{tool_count}_tool_{printer_size}mm"
            print("Generating", name)

            step = os.path.join(step_size_path, f"{name}.step")
            cq.exporters.export(backPlate(printer_size=printer_size, tool_count=tool_count), step)

            stl = os.path.join(stl_size_path, f"{name}.stl")
            cq.exporters.export(backPlate(printer_size=printer_size, tool_count=tool_count), stl, angularTolerance=0.3)

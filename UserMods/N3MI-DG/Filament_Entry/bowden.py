import cadquery as cq


bowden_id = 3
tool_count = 4
panel_thick = 3
split = True
show_ecas = True

ecas04_dia =  8.45
ecas_04_depth = 7.05
ecas04_dia2 =  12
length = 20
clip_holes = [(length/2+(length*i), 0) for i in range(tool_count)]

mount_points = {
    2: [(0, 0.5)],
    3: [(-length*0.5, 0.5), (length*0.5, 0.5)],
    4: [(-length, 0.5), (length, 0.5)],
    5: [(-length*1.5, 0.5), (length*1.5, 0.5)],
    6: [(-length*2, 0.5), (0, 0), (length*2, 0.5)]
}

colours = [
    "green",
    "cyan",
    "magenta",
    "mediumpurple",
    "skyblue2",
    "orange"
]

clip = (
    cq.Workplane()
    .box((length*tool_count)-length/2, 8, 5)
    .translate(((length*tool_count)/2, 0, 0))
    .faces(">Z").workplane().pushPoints(clip_holes).hole(4.05)
    .faces(">Z").workplane(centerOption="CenterOfBoundBox").center(0, 4.52).rect((length*tool_count)-length/2, 5).extrude(-5, "cut")
    .faces(">Y").edges("|Z").fillet(0.5)
    .faces("<Y").edges("|Z").fillet(5)
    .faces(">Z or <Z").chamfer(0.4)
)

bowden_body = (
    cq.Workplane()
    .cylinder(length-1, ecas04_dia/2+3)
    
    .faces(">Z").workplane().circle(ecas04_dia/2+1).extrude(1)

    .faces(">Z").chamfer(0.2)
    .faces(">Z[-2]").edges().chamfer(0.5)
    .faces("<Z").chamfer(0.5)

    .cut(
        cq.Workplane("XZ")
        .polygon(6, length, circumscribed=True)
        .revolve(360, (-((ecas04_dia/2+3)+9), 0, 0), (-((ecas04_dia/2+3)+9), -1, 0))
        .translate((ecas04_dia/2+3+9, 0, 0))
    )

    .cut(
        cq.Workplane("XZ")
        .pushPoints([(10, 0), (-10, 0)])
        .polygon(6, 10, circumscribed=True).extrude(20)
        .translate((0, 10, 0))
    )
)

bowden_body_negative = (
    cq.Workplane()
    .cylinder(length-1, ecas04_dia/2+3.2)
    
    .faces(">Z").workplane().circle(ecas04_dia/2+1.2).extrude(1)

    .faces(">Z").chamfer(0.2)
    .faces(">Z[-2]").edges().chamfer(0.5)
    .faces("<Z").chamfer(0.5)

    .cut(
        cq.Workplane("XZ")
        .polygon(6, length-0.2, circumscribed=True)
        .revolve(360, (-((ecas04_dia/2+3)+9), 0, 0), (-((ecas04_dia/2+3)+9), -1, 0))
        .translate((ecas04_dia/2+3+9, 0, 0))
    )

    .cut(
        cq.Workplane("XZ")
        .pushPoints([(10, 0), (-10, 0)])
        .polygon(6, 10-0.2, circumscribed=True).extrude(20)
        .translate((0, 10, 0))
    )
)

bowden = (
    bowden_body
    .faces(">Z").workplane().hole(bowden_id-0.2)
    .faces(">Z").workplane().hole(ecas04_dia, depth=ecas_04_depth)
    .faces("<Z").edges().item(1).chamfer(4, length/2)

    .faces(cq.NearestToPointSelector((2, 2, length/2-6))).workplane().circle(4.1/2).extrude(-2, "cut")

    .faces(cq.NearestToPointSelector((2, 2, length/2-6))).edges().item(1).chamfer(0.8, 0.2)
    .faces(cq.NearestToPointSelector((0, 0, length/2-8.5))).edges().item(1).chamfer(0.2)
    .edges(cq.NearestToPointSelector((0, 0, length/2-10))).chamfer(0.2)
)

ecas_body =  (
    cq.Workplane()
    .circle(ecas04_dia/2)
    .extrude(ecas_04_depth)
    .faces(">Z").hole(6)
)

ecas_top = (
    cq.Workplane()
    .circle(3)
    .extrude(ecas_04_depth)
    .faces(">Z").workplane().circle(9.8/2).extrude(-1.3)
    .faces(">Z").workplane().hole(4)
    .fillet(0.4)
)


block = (
    cq.Workplane()
    .box(length, length, length-1).translate((0, -1.5, 0))
    .cut(bowden_body_negative if split else bowden_body)
    .faces(">Z").workplane().polygon(4, 12.65).extrude(-length, "cut")
    .faces(">Z").workplane().rect(length, 0.1).extrude(-length, "cut")
    .translate((length/2, 0, 0))
)


if split:
    block = (
        cq.Workplane()
        .box(length, length-3.25, length-1).translate((0, -1.5, 0))
        .cut(bowden_body_negative.translate((0, -3.25/2, 0)))
        .faces(">Z").workplane().center(0, -3.25/2).polygon(4, 12.65).extrude(-length, "cut")
        .faces(">Z").workplane().rect(length, 0.1).extrude(-length, "cut")
        .translate((length/2, 3.25/2, 0))
    )
else:
    block = (
        cq.Workplane()
        .box(length, length-3.25, length-1).translate((0, -1.5, 0))
        .cut(bowden_body.translate((0, -3.25/2, 0)))
        .translate((length/2, 3.25/2, 0))
    )


holder = cq.Workplane()

for i in range(tool_count):
    holder = holder.union(block.translate((length*i, 0, 0)))

holder = (
    holder
    .faces(">Y").edges("|Z").chamfer(6)
    .faces("<Y").workplane(centerOption="CenterOfBoundBox").center(0, 0.5).rect(length*tool_count, 5.8).extrude(panel_thick+1)
    .faces("<Y").edges("|X").chamfer(0.6)
    # .faces("<Y[-2]").workplane(centerOption="CenterOfBoundBox").center(0, 6.4).rect(length*tool_count, 6.5).extrude(-3.25, "cut")
    .faces("<Y[-2]").workplane(centerOption="CenterOfBoundBox").center(0, -6.2).rect(length*tool_count, 7.1).extrude(panel_thick)

    .faces(">Y").workplane(centerOption="CenterOfBoundBox").pushPoints(mount_points[tool_count]).cboreHole(3.2, 5.8, 3.5)
    .faces(">Y").workplane(centerOption="CenterOfBoundBox").pushPoints(mount_points[tool_count]).cskHole(3.2, 6.2, 45)

    .faces(">Z").chamfer(0.4)
    .faces("<Z").chamfer(0.4)
)


def makeSolid():
    global holder
    holder = holder.faces(">X or <X").edges("not(>Z or <Z or >Y)").chamfer(0.4)

    assm = cq.Assembly("Bowden Coupler")
    assm.add(holder, name="Body", color=cq.Color("purple4"))

    for i in range(tool_count):
        assm.add(bowden.translate((length/2+(length*i), 0, 0)), name=f"Tool {i}", color=cq.Color(colours[i]))
        if show_ecas:
            assm.add(ecas_body.translate((length/2+(length*i), 0, length/2-ecas_04_depth+1)), name=f"ECAS04 body {i}", color=cq.Color("gray"))
            assm.add(ecas_top.translate((length/2+(length*i), 0, length/2-ecas_04_depth+3)), name=f"ECAS04 top {i}", color=cq.Color("skyblue3"))

    return assm


def makeSplit():
    bottom  = (
        holder
        .cut(
            cq.Workplane()
            .rect(length*tool_count, 100)
            .extrude(length)
            .translate(((length*tool_count)/2, 50, -length/2))
        )

        .faces(">X or <X").edges("not(>Z or <Z)").chamfer(0.4)
        .faces(">Y").workplane(centerOption="CenterOfBoundBox").pushPoints(mount_points[tool_count]).cskHole(3.2, 3.6, 45)
    )

    top     = (
        holder
        .cut(
            cq.Workplane()
            .rect(length*tool_count, 100)
            .extrude(length)
            .translate(((length*tool_count)/2, -50, -length/2))
        )

        .faces(">X or <X").edges("<Y").chamfer(0.4)
        .faces("<Y").workplane(centerOption="CenterOfBoundBox").pushPoints(mount_points[tool_count]).cskHole(3.2, 3.6, 45)

    )

    cq.exporters.export(top, f"top_{tool_count}tool.stl")
    cq.exporters.export(bottom, f"bottom_{tool_count}tool_{panel_thick}mm.stl")
    cq.exporters.export(top, f"top_{tool_count}tool.step")
    cq.exporters.export(bottom, f"bottom_{tool_count}tool_{panel_thick}mm.step")

    assm = cq.Assembly("Bowden Coupler")
    assm.add(bottom, name="Bottom", color=cq.Color("purple4"))
    assm.add(top, name="Top", color=cq.Color("purple4"))

    for i in range(tool_count):
        assm.add(bowden.translate((length/2+(length*i), 0, 0)), name=f"Tool {i}", color=cq.Color(colours[i]))

        if show_ecas:
            assm.add(ecas_body.translate((length/2+(length*i), 0, length/2-ecas_04_depth+1)), name=f"ECAS04 body {i}", color=cq.Color("gray"))
            assm.add(ecas_top.translate((length/2+(length*i), 0, length/2-ecas_04_depth+3)), name=f"ECAS04 top {i}", color=cq.Color("skyblue3"))

    return assm


# cq.exporters.export(clip, f"clip_{tool_count}tool.stl")
# cq.exporters.export(clip, f"clip_{tool_count}tool.step")
# cq.exporters.export(bowden_body, f"ecas_entry_{bowden_id}mm.stl")
# cq.exporters.export(bowden_body, f"ecas_entry_{bowden_id}mm.step")

if split:
    assm = makeSplit()

    try:
        show_object(assm)
    except NameError:
        assm.save(f"Split_{tool_count}_tool.step")

else:
    assm = makeSolid()

    try:
        show_object(assm)
    except NameError:
        assm.save(f"Solid_{tool_count}_tool_{bowden_id}ID_{panel_thick}mm.step")

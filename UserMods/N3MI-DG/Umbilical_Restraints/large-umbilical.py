import cadquery as cq

cable_dia = 6.35

# Sketches
sk_inner = (
    cq.Sketch()
    .arc((3, 0), 10.8/2, 0, 360)
    .arc((-3, 0), 10.8/2, 0, 360)
    .arc((0, 4.5), 8/2, 0, 360)
    .hull()
)

sk_relief = (
    cq.Sketch()
    .arc((3, 0), 7, 0, 360)
    .arc((-3, 0), 7, 0, 360)
    .arc((0, 4.5), 5.7, 0, 360)
    .hull()
)

sk_clip = (
    cq.Sketch()
    .arc((3, 0), 4.8, 0, 360)
    .arc((-3, 0), 4.8, 0, 360)
    .arc((0, 2), 4.2, 0, 360)
    .hull()
)

def wireRelief():
    return (
        cq.Workplane().placeSketch(sk_inner).extrude(11.5).translate((0, 0, 0))

        .faces(">Z").workplane().placeSketch(sk_relief).extrude(4)
        .faces(">Z").workplane().placeSketch(sk_inner).extrude(30)
        .faces(">Z").chamfer(26, 1)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-7, 0).hole(4.1)
        .faces("<Z").workplane().center(4, -5).hole(1.5)
        .faces("<Z").chamfer(0.5)
        .faces("<Z[-2]").chamfer(0.5)
        .faces(">Z").fillet(0.4)
        .faces(">Z[-2]").fillet(0.799)
        
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, 45), offset=(7, 4, 0))
            .box(10, 1, 100)
        )
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, -45), offset=(-7, 4, 0))
            .box(10, 1, 100)
        )

        .faces("<Y[-2]").workplane().rect(1.2, 16).extrude(-1.2, "cut")
    )

def springRelief():
    return (
        cq.Workplane().placeSketch(sk_inner).extrude(11.5).translate((0, 0, 0))
        .faces(">Z").workplane().placeSketch(sk_relief).extrude(4)
        .faces(">Z").workplane().placeSketch(sk_inner).extrude(30)
        .faces(">Z").chamfer(26, 1)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-7, 0).hole(4.1)
        .faces("<Z").workplane().center(4, -5).rect(3.6, 0.7).cutThruAll()
        .faces("<Z").chamfer(0.5)
        .faces("<Z[-2]").chamfer(0.5)
        .faces(">Z").fillet(0.4)
        .faces(">Z[-2]").fillet(0.799)
        
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, 45), offset=(7, 4, 0))
            .box(10, 1, 100)
        )
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, -45), offset=(-7, 4, 0))
            .box(10, 1, 100)
        )
    )

def springClip():
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(8)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-7, 0).hole(4.1)
        .faces("<Z").workplane().center(4, -4.3).rect(3.6, 0.6).cutThruAll()
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).rect(4.8*2, 0.4).extrude(-8, "cut")
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).polygon(4, 1.2).extrude(-8, "cut")
        .faces("<Z or >Z").chamfer(0.4)
    )

def wireClip():
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(8)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-7, 0).hole(4.1)
        .faces("<Z").workplane().center(4, -4.5).hole(1.5)
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).rect(4.8*2, 0.4).extrude(-8, "cut")
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).polygon(4, 1.2).extrude(-8, "cut")
        .faces("<Z or >Z").chamfer(0.4)
    )

def wireTerminator():
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(26)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-7, 0).hole(4.1)
        .faces("<Z").workplane().center(4, -4.6).hole(1.5, 14)
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).rect(4.8*2, 0.4).extrude(-26, "cut")
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).polygon(4, 1.2).extrude(-26, "cut")
        .faces("<Z").chamfer(0.4)
        .faces(">Z").workplane().center(0, 1.8).rect(20, 5).extrude(-12, "cut")
        .faces(">Z[-2]").edges(">Y").chamfer(0.4, 1)
        .faces("<Y").workplane(centerOption="CenterOfBoundBox").rect(1.5, 10).extrude(-1.5, "cut")
        .faces("<Y").workplane(centerOption="CenterOfBoundBox").center(0, 4.8).rect(1.5, 8).extrude(-10, "cut")
        .faces(">Y[-1]").edges("|X").item(0).chamfer(2, 1)
        .faces(">Z").chamfer(0.2)
    )

def springTerminator():
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(26)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-7, 0).hole(4.1)
        .faces("<Z").workplane().center(4, -4.25).rect(3.6, 0.6).cutThruAll()
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).rect(4.8*2, 0.4).extrude(-26, "cut")
        .faces(">Z").workplane().pushPoints([(3+4.8, -4.3), (-(3+4.8), -4.3)]).polygon(4, 1.2).extrude(-26, "cut")
        .faces("<Z").chamfer(0.4)
        .faces(">Z").workplane().center(0, 2.2).rect(20, 5).extrude(-12, "cut")
        .faces(">Z[-2]").edges(">Y").chamfer(0.4, 1)
        .faces("<Y").workplane(centerOption="CenterOfBoundBox", offset=-8.8).center(0, 5.8).rect(4.5, 10).extrude(0.5, "cut")
        .faces(">Z").chamfer(0.2)
    )


try:
    show_object(springTerminator())

except NameError:
    # if run via commandline export for release
    import os
    current_path = os.getcwd()
    stl_path     = os.path.join(current_path, "STL")
    step_path    = os.path.join(current_path, "STEP")
    stl_large    = os.path.join(stl_path, "Large")
    step_large   = os.path.join(step_path, "Large")

    for x in [stl_path, step_path, stl_large, step_large]:
        if not os.path.exists(x):
            os.makedirs(x)
    

    for type in ["spring", "wire"]:
        type_stl  = os.path.join(stl_large, type.title())
        type_step = os.path.join(step_large, type.title())

        for x in [type_stl, type_step]:
            if not os.path.exists(x):
                os.makedirs(x)

        for item in ["Relief", "Clip", "Terminator"]:
            for cable_dia in [3.7, 4, 4.5, 5, 5.5, 6, 6.35]:
                cable_stl  = os.path.join(type_stl, f"{cable_dia}mm Cable")
                cable_step = os.path.join(type_step, f"{cable_dia}mm Cable")

                for x in [cable_stl, cable_step]:
                    if not os.path.exists(x):
                        os.makedirs(x)

                name = f"Large_{type.title()}_{item}_{cable_dia}mm_Cable"
                
                print("Generating", name)

                step = os.path.join(cable_step, f"{name}.step")
                cq.exporters.export(locals()[f"{type}{item}"](), step)

                stl = os.path.join(cable_stl, f"{name}.stl")
                cq.exporters.export(locals()[f"{type}{item}"](), stl, angularTolerance=0.3)
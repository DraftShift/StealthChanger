import cadquery as cq

# Sketches
sk_inner = (
    cq.Sketch()
    .arc((3, 0), 3.55, 0, 360)
    .arc((-3, 0), 3.55, 0, 360)
    .arc((0, 3), 2.1, 0, 360)
    .hull()
)

sk_relief = (
    cq.Sketch()
    .arc((3, 0), 5.15, 0, 360)
    .arc((-3, 0), 5.15, 0, 360)
    .arc((0, 3), 3.8, 0, 360)
    .hull()
)

sk_clip = (
    cq.Sketch()
    .arc((3, 0), 3, 0, 360)
    .arc((-3, 0), 3, 0, 360)
    .arc((0, 2), 3, 0, 360)
    .hull()
)

def wireRelief(cable_dia=3.7):
    return (
        cq.Workplane().placeSketch(sk_inner).extrude(11.5).translate((0, 0, 0))

        .faces(">Z").workplane().placeSketch(sk_relief).extrude(4)
        .faces(">Z").workplane().placeSketch(sk_inner).extrude(21)
        .faces(">Z").chamfer(17, 0.5)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-6, 0).hole(4.1)
        .faces("<Z").workplane().center(3, -3).hole(1.5)
        .faces("<Z").chamfer(0.3)
        .faces("<Z[-2]").chamfer(0.5)
        .faces(">Z").fillet(0.2)
        .faces(">Z[-2]").fillet(0.799)
        
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, 45), offset=(6, 3, 0))
            .box(10, 1, 100)
        )
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, -45), offset=(-6, 3, 0))
            .box(10, 1, 100)
        )

        .faces("<Y[-2]").workplane().rect(1.2, 16).extrude(-1.2, "cut")
    )

def springRelief(cable_dia=3.7):
    return (
        cq.Workplane().placeSketch(sk_inner).extrude(11.5).translate((0, 0, 0))

        .faces(">Z").workplane().placeSketch(sk_relief).extrude(4)
        .faces(">Z").workplane().placeSketch(sk_inner).extrude(21)
        .faces(">Z").chamfer(17, 0.5)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-6, 0).hole(4.1)
        .faces("<Z").workplane().center(3, -3).rect(3.6, 0.6).cutThruAll()
        .faces("<Z").chamfer(0.3)
        .faces("<Z[-2]").chamfer(0.5)
        .faces(">Z").fillet(0.2)
        .faces(">Z[-2]").fillet(0.799)
        
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, 45), offset=(6, 3, 0))
            .box(10, 1, 100)
        )
        .cut(
            cq.Workplane()
            .transformed(rotate=(0, 0, -45), offset=(-6, 3, 0))
            .box(10, 1, 100)
        )
    )

def springClip(cable_dia=3.7):
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(8)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-6, 0).hole(4.1)
        .faces("<Z").workplane().center(3, -3).rect(3.6, 0.6).cutThruAll()
        .faces(">Z").workplane().pushPoints([(3+3, -3), (-(3+3), -3)]).rect(3*2, 0.4).extrude(-26, "cut")
        .faces(">Z").workplane().pushPoints([(3+3, -3), (-(3+3), -3)]).polygon(4, 1.2).extrude(-26, "cut")
        .faces("<Z or >Z").chamfer(0.2)
    )

def wireClip(cable_dia=3.7):
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(8)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-6, 0).hole(4.1)
        .faces("<Z").workplane().center(3, -3).hole(1.5)
        .faces(">Z").workplane().pushPoints([(3+3, -3), (-(3+3), -3)]).rect(3*2, 0.4).extrude(-26, "cut")
        .faces(">Z").workplane().pushPoints([(3+3, -3), (-(3+3), -3)]).polygon(4, 1.2).extrude(-26, "cut")
        .faces("<Z or >Z").chamfer(0.2)
    )

def wireTerminator(cable_dia=3.7):
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(26)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-6, 0).hole(4.1)
        .faces("<Z").workplane().center(3, -3.5).hole(1.5, 14)
        .faces(">Z").workplane().pushPoints([(3+3, -3.3), (-(3+3), -3.3)]).rect(3*2, 0.4).extrude(-26, "cut")
        .faces(">Z").workplane().pushPoints([(3+3, -3.25), (-(3+3), -3.25)]).polygon(4, 1.2).extrude(-26, "cut")
        .faces("<Z").chamfer(0.2)
        .faces(">Z").workplane().center(0, 1.9).rect(20, 5).extrude(-12, "cut")
        .faces(">Z[-2]").edges(">Y").chamfer(0.5, 1)
        .faces("<Y").workplane(centerOption="CenterOfBoundBox").rect(1.5, 10).extrude(-1.5, "cut")
        .faces("<Y").workplane(centerOption="CenterOfBoundBox").center(0, 4.9).rect(1.5, 8).extrude(-10, "cut")
        .faces("<Y").workplane(centerOption="CenterOfBoundBox", offset=-2.25).center(0, 4.9).rect(6, 8).extrude(-1.5, "cut")
        .faces(">Z").chamfer(0.2)
        .faces(">Y[-1]").edges("|X").item(-1).chamfer(3, 1.25)
    )

def springTerminator(cable_dia=3.7):
    return (
        cq.Workplane().placeSketch(sk_clip).extrude(26)
        .faces("<Z").workplane().center(3, 0).hole(cable_dia)
        .faces("<Z").workplane().center(-6, 0).hole(4.1)
        .faces("<Z").workplane().center(3, -3).rect(3.6, 0.6).extrude(-14, "cut")
        .faces(">Z").workplane().pushPoints([(3+3, -3), (-(3+3), -3)]).rect(3*2, 0.4).extrude(-26, "cut")
        .faces(">Z").workplane().pushPoints([(3+3, -3), (-(3+3), -3)]).polygon(4, 1.2).extrude(-26, "cut")
        .faces("<Z").chamfer(0.2)
        .faces(">Z").workplane().center(0, 2.5).rect(20, 5).extrude(-12, "cut")
        .faces(">Z[-2]").edges(">Y").chamfer(0.4, 1)
        .faces(">Z").chamfer(0.2)
        .faces("<Y").workplane(centerOption="CenterOfBoundBox", offset=-6).center(0, 6).rect(4.5, 10).extrude(0.5, "cut")
    )


try:
    show_object(springClip())

# except NameError:
#     # if run via commandline export for release
#     import os
#     current_path = os.getcwd()
#     stl_path     = os.path.join(current_path, "STL")
#     step_path    = os.path.join(current_path, "STEP")

#     for x in [stl_path, step_path]:
#         if not os.path.exists(x):
#             os.makedirs(x)
    

    # for type in ["spring", "wire"]:
    #     for item in ["Relief", "Clip", "Terminator"]:
    #         for cable_dia in [3.7, 4, 4.5]:

    #             name = f"Tapchanger_{type.title()}_{item}_{cable_dia}mm"
    #             print("Generating", name)
    #             step = os.path.join(step_path, f"{name}.step")
    #             cq.exporters.export(locals()[f"{type}{item}"](cable_dia), step)

    #             stl = os.path.join(stl_path, f"{name}.stl")
    #             cq.exporters.export(locals()[f"{type}{item}"](cable_dia), stl, angularTolerance=0.3)

except NameError:
        # if run via commandline export for release
        import os
        current_path = os.getcwd()
        stl_path     = os.path.join(current_path, "STL")
        step_path    = os.path.join(current_path, "STEP")
        stl_regular    = os.path.join(stl_path, "Regular")
        step_regular   = os.path.join(step_path, "Regular")

        for x in [stl_path, step_path, stl_regular, step_regular]:
            if not os.path.exists(x):
                os.makedirs(x)
        

        for type in ["spring", "wire"]:
            type_stl  = os.path.join(stl_regular, type.title())
            type_step = os.path.join(step_regular, type.title())

            for x in [type_stl, type_step]:
                if not os.path.exists(x):
                    os.makedirs(x)

            for item in ["Relief", "Clip", "Terminator"]:
                for cable_dia in [3.7, 4, 4.5]:
                    cable_stl  = os.path.join(type_stl, f"{cable_dia}mm Cable")
                    cable_step = os.path.join(type_step, f"{cable_dia}mm Cable")

                    for x in [cable_stl, cable_step]:
                        if not os.path.exists(x):
                            os.makedirs(x)

                    name = f"Regular_{type.title()}_{item}_{cable_dia}mm_Cable"
                    
                    print("Generating", name)

                    step = os.path.join(cable_step, f"{name}.step")
                    cq.exporters.export(locals()[f"{type}{item}"](), step)

                    stl = os.path.join(cable_stl, f"{name}.stl")
                    cq.exporters.export(locals()[f"{type}{item}"](), stl, angularTolerance=0.3)
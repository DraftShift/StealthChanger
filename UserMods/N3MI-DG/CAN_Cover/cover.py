import cadquery as cq

profiles = {
    "fly_utoc": {
        "inside_y": 70, 
        "mount_points": [
            (79.330/2+5, 19.230/2+10), 
            (-79.330/2+5, 19.230/2+10), 
            (-79.330/2+5, -19.230/2+10), 
            (79.330/2+5, -19.230/2+10)
        ]
    },
    "btt_ceb": {
        "inside_y": 70, 
        "mount_points": [
            ((-137.5/2)+61.75, (10-3.5)+22), 
            ((-137.5/2)+3.5, (10-3.5)+22), 
            (137.5/2-3.25, 22)
        ]
    },
    "duel_btt_ceb": {
        "inside_y": 100, 
        "mount_points": [
            ((-137.5/2)+61.75, (10-3.5)+37), 
            ((-137.5/2)+3.5, (10-3.5)+37), 
            (137.5/2-3.25, 37), 
            ((137.5/2)-61.75, -43.5), 
            ((137.5/2)-3.5, -43.5), 
            (-(137.5/2)+3.25, -(43.5-6.5))
        ]
    },
    "btt_u2c": {
        "inside_y": 70, 
        "mount_points": [
            ((85.45/2)-3.06, 19.23/2+15), 
            ((85.45/2)-3.06, -19.23/2+15), 
            ((-85.45/2)+3.06, 19.23/2+15), 
            ((-85.45/2)+3.06, -19.23/2+15)
        ]
    },
    "btt_u2c_ceb": {
        "inside_y": 100, 
        "mount_points": [
            ((85.45/2)-3.06, 19.23/2+25), 
            ((85.45/2)-3.06, -19.23/2+25), 
            ((-85.45/2)+3.06, 19.23/2+25), 
            ((-85.45/2)+3.06, -19.23/2+25),
            ((137.5/2)-61.75, -43.5), 
            ((137.5/2)-3.5, -43.5), 
            (-(137.5/2)+3.25, -(43.5-6.5))
        ]
    },
    "fly_utoc_btt_ceb": {
        "inside_y": 100, 
        "mount_points": [
            (79.330/2+5, 19.230/2+20), 
            (-79.330/2+5, 19.230/2+20), 
            (-79.330/2+5, -19.230/2+20), 
            (79.330/2+5, -19.230/2+20),
            ((137.5/2)-61.75, -43.5), 
            ((137.5/2)-3.5, -43.5), 
            (-(137.5/2)+3.25, -(43.5-6.5))
        ]
    },
    "pi_btt_ceb": {
        "inside_y": 130, 
        "mount_points": [
            (58/2-28, 49/2+25), 
            (-58/2-28, 49/2+25), 
            (-58/2-28, -49/2+25), 
            (58/2-28, -49/2+25),

            ((137.5/2)-61.75, -58.5), 
            ((137.5/2)-3.5, -58.5), 
            (-(137.5/2)+3.25, -(58.5-6.5))
        ]
    }
}

bowden_clearance = 25
wall             = 1.6
panel_offset     = wall+12.9


def makeCover(profile, panel_clearance):
    inside_x           = 146
    inside_y           = profiles[profile]["inside_y"]
    inside_z           = 42
    board_mount_points = profiles[profile]["mount_points"]

    bottom_mount = [
        (134/2, inside_y/2-((panel_offset-(panel_offset-wall-10))+37.068)+wall),
        (-134/2, inside_y/2-((panel_offset-(panel_offset-wall-10))+37.068)+wall)
    ]

    cover = (
        # Create Shell
        cq.Workplane()
        .rect(inside_x, inside_y)
        .extrude(inside_z).edges("|Z").fillet(3.6)
        .faces("+Z").shell(wall)

        # Board Mount
        .faces(cq.NearestToPointSelector((0, 0, 0)))
        .workplane(centerOption="CenterOfBoundBox")
        .pushPoints(board_mount_points)
        .circle(3)
        .extrude(5)

        .faces(cq.NearestToPointSelector((0, 0, 0)))
        .workplane(centerOption="CenterOfBoundBox", offset=5)
        .pushPoints(board_mount_points)
        .cskHole(2.85, 3.2, 45, 5)

        # Fillet Inner
        .faces(cq.NearestToPointSelector((0, 0, 0))).fillet(wall)

        # Cable Clearance
        .cut(
            cq.Workplane()
            .box(inside_x-15, inside_y, inside_z)
            .translate((0, -inside_y/2, (inside_z*1.5)-(panel_clearance+bowden_clearance)))
            .edges("|Y").chamfer(6)
        )

        # Panel Clearance
        .cut(
            cq.Workplane()
            .box(inside_x+(wall*2), inside_y+(wall*2), inside_z)
            .translate((0, -panel_offset, (inside_z*1.5)-panel_clearance))
        )

        # Top Mount
        .union(
            cq.Workplane()
            .circle(5).extrude(inside_z)
            .faces(">Z").workplane().center(0, 5).rect(10, 10).extrude(-inside_z)
            .cut(
                cq.Workplane().transformed(rotate=(30, 0, 0))
                .box(20, 28, inside_z*2)
                .translate((0, 0, -7))
            )
            .translate((0, inside_y/2-10, 0))
        )

        .cut(
            cq.Workplane()
            .circle(5-wall).extrude(inside_z)
            .faces(">Z").workplane().center(0, 5+wall/2).rect(10-(wall*2), 10+wall).extrude(-inside_z)
            .cut(
                cq.Workplane().transformed(rotate=(30, 0, 0))
                .box(20, 28, inside_z*2)
                .translate((0, 0, wall-7))
            )
            .translate((0, inside_y/2-10, wall))
        )

        .union(
            cq.Workplane()
            .circle(5).extrude(wall)
            .faces(">Z").workplane().center(0, 5+(wall/2)).rect(10, 10+wall).extrude(-wall)
            .faces(">Z").workplane().center(0, -(5+(wall/2))).hole(3.2)
            .faces("<Z").workplane().rect(3.2, 3.2).extrude(-0.4, "cut")
            .faces("<Z").workplane().rect(10, 3.2).extrude(-0.2, "cut")
            .translate((0, inside_y/2-10, inside_z-wall))
        )

        .edges(cq.NearestToPointSelector((0, inside_y/2, 13))).fillet(wall)
        .edges(cq.NearestToPointSelector((-8, inside_y/2, 23))).fillet(wall)
        .edges(cq.NearestToPointSelector((8, inside_y/2, 23))).fillet(wall)
        .faces(cq.NearestToPointSelector((0, inside_y/2-wall*6, 13))).fillet(wall*2)
        .edges(cq.NearestToPointSelector((0, inside_y/2+wall*2, 23))).fillet(wall*2)

        # Bottom Mount
        .union(
            cq.Workplane()
            .circle(5).extrude(inside_z)
            .faces(">Z").workplane().center((inside_x/2-bottom_mount[0][0])/2, 0).rect((inside_x/2-bottom_mount[0][0]), 10).extrude(-inside_z)
            .cut(
                cq.Workplane().transformed(rotate=(0, -30, 0))
                .box(28, 20, inside_z*2)
                .translate((0, 0, -5))
            )
            .translate((bottom_mount[0][0], bottom_mount[0][1], -5))
        )

        .cut(
            cq.Workplane()
            .circle(5-wall).extrude(inside_z)
            .faces(">Z").workplane().center(((inside_x/2-bottom_mount[0][0])/2)+wall/2, 0).rect(((inside_x/2-bottom_mount[0][0]))+wall, 10-(wall*2)).extrude(-inside_z)
            .cut(
                cq.Workplane().transformed(rotate=(0, -30, 0))
                .box(28, 20, inside_z*2)
                .translate((0, 0, wall-5))
            )
            .translate((bottom_mount[0][0], bottom_mount[0][1], wall-5))
            .faces(">Z").wires().toPending().extrude(-wall, "cut")
        )

        .union(
            cq.Workplane()
            .circle(5).extrude(wall)
            .faces(">Z").workplane().center(((inside_x/2-bottom_mount[0][0])/2)+wall/2, 0).rect(((inside_x/2-bottom_mount[0][0]))+wall, 10).extrude(-wall)
            .faces(">Z").workplane().center(-((inside_x/2-bottom_mount[0][0])/2)-wall/2, 0).hole(3.2)
            .faces("<Z").workplane().rect(3.2, 3.2).extrude(-0.4, "cut")
            .faces("<Z").workplane().rect(3.2, 10).extrude(-0.2, "cut")
            .translate((bottom_mount[0][0], bottom_mount[0][1], inside_z-(wall+5)))
        )

        .edges(cq.NearestToPointSelector((inside_x/2, bottom_mount[0][1], 15))).fillet(wall)
        .edges(cq.NearestToPointSelector((inside_x/2, bottom_mount[0][1]-8, 25))).fillet(wall)
        .edges(cq.NearestToPointSelector((inside_x/2, bottom_mount[0][1]+8, 25))).fillet(wall)
        .faces(cq.NearestToPointSelector((inside_x/2-wall*4, bottom_mount[0][1], 15))).fillet(wall*2)
        .edges(cq.NearestToPointSelector((inside_x/2+wall*2, bottom_mount[0][1]+5, 25))).fillet(wall*2)

        .union(
            cq.Workplane()
            .circle(5).extrude(inside_z)
            .faces(">Z").workplane().center(-(inside_x/2-bottom_mount[0][0])/2, 0).rect((inside_x/2-bottom_mount[0][0]), 10).extrude(-inside_z)
            .cut(
                cq.Workplane().transformed(rotate=(0, 30, 0))
                .box(28, 20, inside_z*2)
                .translate((0, 0, -5))
            )
            .translate((bottom_mount[1][0], bottom_mount[1][1], -5))
        )

        .cut(
            cq.Workplane()
            .circle(5-wall).extrude(inside_z)
            .faces(">Z").workplane().center(-((inside_x/2-bottom_mount[0][0])/2)-wall/2, 0).rect(-((inside_x/2-bottom_mount[0][0]))-wall, 10-(wall*2)).extrude(-inside_z)
            .cut(
                cq.Workplane().transformed(rotate=(0, 30, 0))
                .box(28, 20, inside_z*2)
                .translate((0, 0, wall-5))
            )
            .translate((bottom_mount[1][0], bottom_mount[1][1], wall-5))
            .faces(">Z").wires().toPending().extrude(-wall, "cut")
        )

        .union(
            cq.Workplane()
            .circle(5).extrude(wall)
            .faces(">Z").workplane().center(-((inside_x/2-bottom_mount[0][0])/2)-wall/2, 0).rect(-((inside_x/2-bottom_mount[0][0]))-wall, 10).extrude(-wall)
            .faces(">Z").workplane().center(((inside_x/2-bottom_mount[0][0])/2)+wall/2, 0).hole(3.2)
            .faces("<Z").workplane().rect(3.2, 3.2).extrude(-0.4, "cut")
            .faces("<Z").workplane().rect(3.2, 10).extrude(-0.2, "cut")
            .translate((bottom_mount[1][0], bottom_mount[1][1], inside_z-(wall+5)))
        )

        .edges(cq.NearestToPointSelector((-(inside_x/2), bottom_mount[0][1], 15))).fillet(wall)
        .edges(cq.NearestToPointSelector((-(inside_x/2), bottom_mount[0][1]-8, 25))).fillet(wall)
        .edges(cq.NearestToPointSelector((-(inside_x/2), bottom_mount[0][1]+8, 25))).fillet(wall)
        .faces(cq.NearestToPointSelector((-(inside_x/2-wall*4), bottom_mount[0][1], 15))).fillet(wall*2)
        .edges(cq.NearestToPointSelector((-(inside_x/2+wall*2), bottom_mount[0][1]+5, 25))).fillet(wall*2)

    )
    return cover


try:
    show_object(makeCover("fly_utoc", panel_clearance=3))
except NameError:

    # Release
    import os
    current_path = os.getcwd()
    stl_path     = os.path.join(current_path, "STL")
    step_path    = os.path.join(current_path, "STEP")

    for x in [stl_path, step_path]:
        if not os.path.exists(x):
            os.makedirs(x)

    for profile in profiles:
        profile_path_stl  = os.path.join(stl_path, profile.upper())
        profile_path_step = os.path.join(step_path, profile.upper())

        for x in [profile_path_stl, profile_path_step]:
            if not os.path.exists(x):
                os.makedirs(x)

        for panel_clearance in [3, 3.5, 4, 4.5, 5]:
            fn    = f"{profile.upper()}_{panel_clearance}mm_panel_gap"
            cover = makeCover(profile, panel_clearance)
            stl   = os.path.join(profile_path_stl, f"{fn}.stl")
            step  = os.path.join(profile_path_step, f"{fn}.step")

            print("Exporting", stl)
            cq.exporters.export(cover, stl, angularTolerance=0.3)

            print("Exporting", step)
            cq.exporters.export(cover, step)

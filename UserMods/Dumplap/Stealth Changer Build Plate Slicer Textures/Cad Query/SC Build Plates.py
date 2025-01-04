import cadquery as cq
from cadquery import exporters

# Build Plate Dimensions
X = 300
Y = 300

Xoffset = X - (X / 35)
Yoffset = X / 35
Logo_Height = 1

# Draft Shift Design Logo polylines
pts = [
[(-23.10 * 2 - (-23.10 - Xoffset), 36.67 + Yoffset), (-23.10 * 2 - (-8.66 - Xoffset), 28.33 + Yoffset), (-23.10 * 2 - (-5.78 - Xoffset), 30.00 + Yoffset), (-23.10 * 2 - (-23.10 - Xoffset), 40.00 + Yoffset), (-23.10 * 2 - (-40.42 - Xoffset), 30.00 + Yoffset), (-23.10 * 2 - (-40.42 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (-46.19 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (-40.42 - Xoffset), 14.23 + Yoffset), (-23.10 * 2 - (-37.53 - Xoffset), 15.89 + Yoffset), (-23.10 * 2 - (-37.53 - Xoffset), 28.33 + Yoffset)],
[(-23.10 * 2 - (-8.66 - Xoffset), 24.11 + Yoffset), (-23.10 * 2 - (-8.66 - Xoffset), 11.67 + Yoffset), (-23.10 * 2 - (-23.10 - Xoffset), 3.33 + Yoffset), (-23.10 * 2 - (-37.53 - Xoffset), 11.67 + Yoffset), (-23.10 * 2 - (-40.42 - Xoffset), 10.00 + Yoffset), (-23.10 * 2 - (-23.10 - Xoffset), 0.00 + Yoffset), (-23.10 * 2 - (-5.78 - Xoffset), 10.00 + Yoffset), (-23.10 * 2 - (-5.78 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (0.00 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (-5.78 - Xoffset), 25.77 + Yoffset)],
[(-23.10 * 2 - (-23.10 - Xoffset), 10.00 + Yoffset), (-23.10 * 2 - (-27.30 - Xoffset), 10.00 + Yoffset), (-23.10 * 2 - (-33.59 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (-29.40 - Xoffset), 20.00 + Yoffset)],
[(-23.10 * 2 - (-27.30 - Xoffset), 30.00 + Yoffset), (-23.10 * 2 - (-31.49 - Xoffset), 30.00 + Yoffset), (-23.10 * 2 - (-18.90 - Xoffset), 10.00 + Yoffset), (-23.10 * 2 - (-14.70 - Xoffset), 10.00 + Yoffset)],
[(-23.10 * 2 - (-12.60 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (-16.80 - Xoffset), 20.00 + Yoffset), (-23.10 * 2 - (-23.10 - Xoffset), 30.00 + Yoffset), (-23.10 * 2 - (-18.90 - Xoffset), 30.00 + Yoffset)]
]


# 'Extrude' DSD Logo
result = cq.Workplane("XY")
for polyline in pts:
    result = result.polyline(polyline).close().extrude(Logo_Height)

# Create the bounding rectangle
rectangle_pts = [
    (0, 0),  # Bottom-left corner
    (0, Y),  # Top-left corner
    (X, Y),  # Top-right corner
    (X, 0)  # Bottom-right corner
]

result = result.polyline(rectangle_pts).close().extrude(Logo_Height / 2)

# Export the result to SVG
exporters.export(
    result,
    f'<YOUR_OUTPUT_DEST>/SC Plate {X}x{Y}.svg',
    opt={
        "width": X,
        "height": Y,
        "marginLeft": 0,
        "marginTop": 0,
        "showAxes": False,
        "projectionDir": (0, 0, 1),
        "strokeWidth": 0.25,
        "strokeColor": (255, 0, 0),
        "hiddenColor": (0, 0, 255),
        "showHidden": False,
    }
)
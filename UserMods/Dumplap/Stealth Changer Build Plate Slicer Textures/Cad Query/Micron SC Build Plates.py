import cadquery as cq
from cadquery import exporters

# Build Plate Dimensions
X = 180
Y = 180

Xoffset = X - (X / 35)
Yoffset = X / 35
Logo_Height = 1

# Draft Shift Design Logo polylines
pts = shifted_polylines =  [
[(-35.0000 + Xoffset, 25.9808 + Yoffset),(-20.0000 + Xoffset, 34.6400 + Yoffset),(-5.0000 + Xoffset, 25.9808 + Yoffset),(-5.0000 + Xoffset, 17.3205 + Yoffset),(0.0000 + Xoffset, 17.3205 + Yoffset),(-5.0000 + Xoffset, 12.3205 + Yoffset),(-7.5000 + Xoffset, 13.7638 + Yoffset),(-7.5000 + Xoffset, 24.5363 + Yoffset),(-20.0000 + Xoffset, 31.7543 + Yoffset),(-32.5000 + Xoffset, 24.5363 + Yoffset)],
[(-5.0000 + Xoffset, 8.6602 + Yoffset),(-20.0000 + Xoffset, 0.0000 + Yoffset),(-35.0000 + Xoffset, 8.6602 + Yoffset),(-35.0000 + Xoffset, 17.3205 + Yoffset),(-40.0000 + Xoffset, 17.3205 + Yoffset),(-35.0000 + Xoffset, 22.3205 + Yoffset),(-32.5000 + Xoffset, 20.8771 + Yoffset),(-32.5000 + Xoffset, 10.1036 + Yoffset),(-20.0000 + Xoffset, 2.8867 + Yoffset),(-8.5000 + Xoffset, 10.1036 + Yoffset)],
[(-20.2389 + Xoffset, 24.6848 + Yoffset),(-28.7334 + Xoffset, 11.7811 + Yoffset),(-29.7182 + Xoffset, 10.2844 + Yoffset),(-26.4598 + Xoffset, 10.2844 + Yoffset),(-23.3929 + Xoffset, 14.9430 + Yoffset),(-16.9468 + Xoffset, 14.9430 + Yoffset),(-13.6513 + Xoffset, 14.9430 + Yoffset),(-15.2736 + Xoffset, 17.4845 + Yoffset),(-10.5337 + Xoffset, 24.6848 + Yoffset),(-13.8797 + Xoffset, 24.6848 + Yoffset),(-18.6198 + Xoffset, 17.4845 + Yoffset),(-21.7198 + Xoffset, 17.4845 + Yoffset),(-16.9799 + Xoffset, 24.6845 + Yoffset)]
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
    f'<YOUR_OUTPUT_DEST>/Micron SC Plate {X}x{Y}.svg',
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
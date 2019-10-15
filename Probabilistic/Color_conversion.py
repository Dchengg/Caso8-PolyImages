from colormath.color_objects import XYZColor, sRGBColor,LabColor
from colormath.color_conversions import convert_color

rgb = sRGBColor(82, 103, 20)
xyz = convert_color(rgb, XYZColor)
lab = convert_color(xyz,LabColor)
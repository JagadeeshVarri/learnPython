# Write a Python program to get the volume of a sphere with radius 6.

import math

radius = int(input("Enter the radius of ths sphere to know the volume : "))
pie = 3.14159265
volume = (4.0/3.0)*pie*(radius**3)
print(f"The volume of the sphere {volume}")
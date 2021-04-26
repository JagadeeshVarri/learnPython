# Write a Python program that will accept the base and height of a triangle and compute the area

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))

def area_of_triangle(b,h):
    return 0.5*b*h

print(area_of_triangle(base, height))
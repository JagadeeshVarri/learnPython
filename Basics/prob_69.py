# Write a Python program to sort three integers without using conditional statements and loops

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

min = min(x, y, z)
max = max(x, y, z)
mid = (x + y + z) - min - max
print("sorted order: ", min, mid, max)
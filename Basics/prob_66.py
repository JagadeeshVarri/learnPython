# Write a Python program to calculate body mass index

height = float(input("Enter your height in Feet: "))
weight = float(input("Enter your weight in Kilogram: "))
print("Your body mass index is: ", round(weight / (height * height), 2))

# Write a Python program to convert height (in feet and inches) to centimeters
#1 foot = 30.48 cm
print("Enter your height: ")
feet = int(input("enter you feet : "))
inches = int(input("enter you Inches : "))

feet = feet+(inches/12)
cms = round(feet*30.48)

print(f"your height is : {cms} cm.")

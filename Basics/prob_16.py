# Write a Python program 
# to get the difference between a given number and 17
# if the number is greater than 17 return double the absolute difference.

value= int(input("enter the value: "))
if value < 17:
    difference = 17 - value
    print(difference)
elif value > 17:
    difference = value - 17
    print(difference*2)


# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

value = int(input("Enter a value to know Odd or Even : "))

def odd_or_even(value):
    if value%2==0:
        print(f"{value} is Even Number")
    else:
        print(f"{value} is Odd Number")

odd_or_even(value)
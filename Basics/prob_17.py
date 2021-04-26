# Write a Python program to test whether a number is within 100 of 1000 or 2000.
n = int(input("enter a value: "))

def within(n):
    value = ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
    print(value)

within(n)
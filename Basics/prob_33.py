# Write a Python program to sum of three given integers. However,
# if two values are equal sum will be zero.

val1 = int(input("Enter a value: "))
val2 = int(input("Enter a value: "))
val3 = int(input("Enter a value: "))

def check(val1, val2, val3):
    if (val1 == val2) or (val2 == val3):
        sum = 0
    else:
        sum = val1+val2+val3
    
    return sum

print(check(val1, val2, val3))

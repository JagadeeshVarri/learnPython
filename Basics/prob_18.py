# Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

value_1 = int(input("Enter a value: "))
value_2 = int(input("Enter a value: "))
value_3 = int(input("Enter a value: "))

if value_1==value_2 and value_2 ==value_3:
    print((value_1+value_2+value_3)*3)
else:
    print(value_1+value_2+value_3)

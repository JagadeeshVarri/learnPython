# Write a python program to find the sum of the first n positive integers

num = int(input("enter a value:"))

def sum(num):
    val = (num*(num+1))/2
    return int(val)

print(f"The sum of first {num} numbers is ",sum(num))
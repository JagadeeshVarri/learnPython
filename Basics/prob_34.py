# Write a Python program to sum of two given integers. 
# However, if the sum is between 15 to 20 it will return 20


val1 = int(input("Enter a value : "))
val2 = int(input("Enter a value : "))

sum = val1+val2
if (sum>15) or (sum<20):
    print(20)
else:
    print(sum)
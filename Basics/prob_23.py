# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
copy = int(input("Enter no' of copies: "))
str1 = input("Enter a string : ")
length = len(str1)


def copies(copy,str1):
    if length<2:
        print(str1*copy)
    else:
        print(str1[:2]*copy)

copies(copy, str1)
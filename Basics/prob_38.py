# Write a Python program to add two objects if both objects are an integer type

def int_obj(val1, val2):
    if type(val1) == type(val2):
        return val1+val2
    else:
        return "both should be integer "


print(int_obj(9, 9.0))
# Write a Python program to concatenate all elements in a list into a string and return it

def list_string(list1):
    string =" "
    for item in list1:  
        string = string + str(item)
    return string

print(list_string([1,2,3,45]))
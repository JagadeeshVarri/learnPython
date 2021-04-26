# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

values = input("Enter values separated by commas',' : ")
store_list = values.split(",")
store_tuple = tuple(store_list)
print('List : ',store_list)
print('Tuple : ',store_tuple)
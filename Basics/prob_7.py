# Write a Python program to accept a filename from the user and print the extension of that.

file_name = input("Enter file name with extension : ")

file_extension = file_name.split('.')[1]

print(file_extension)
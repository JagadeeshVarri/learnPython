# Write a Python program to check whether a specified value is contained in a group of values.

def search(data, n):
    for value in data:
        if n == value:
            return True
    return False
print(search([1, 5, 8, 3], 3))
print(search([5, 8, 3], 9))
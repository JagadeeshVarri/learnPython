# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

def test(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False;
print(test([1,2,2,5,7,9]))
print(test([2,4,5,7,9]))
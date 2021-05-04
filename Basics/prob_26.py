# Write a Python program to create a histogram from a given list of integers

def histogram( items ):
    for n in items:
        output = '* '
        times = n
        print(output*n)

histogram([3, 2, 5, 6])
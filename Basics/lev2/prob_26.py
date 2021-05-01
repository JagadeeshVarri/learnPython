# Write a Python program to find the type of the progression (arithmetic progression/geometric progression) and the next successive member of a given three successive members of a sequence.

def progression(arr):
    if arr[0]==arr[1]==arr[2]==0:
        return "Wrong Numbers"
    else:
        if arr[1]-arr[0]==arr[2]-arr[1]:
            n=2*arr[2]-arr[1]
            return "AP sequence, "+'Next number of the sequence: '+str(n)
        else:
            n=arr[2]**2/arr[1]
            return "GP sequence, " + 'Next number of the sequence:  '+str(n)

print(progression([1,2,3]))
print(progression([2,6,18]))
print(progression([0,0,0]))

# Write a Python program to compute 
# the greatest common divisor (GCD) of two positive integers

val1 = int(input("Enter a value : "))
val2 = int(input("Enter a value : "))

def get_gcd(val1, val2):
    gcd = 1

    if val1%val2 == 0:
        return val2
    
    for val in range(int(val2/2),0,-1):
        if val1 % val == 0 and val2%val==0:
            gcd = val
        
    return gcd

print(get_gcd(val1, val2))
    
# Write a Python program to get execution time for a Python method
import time
def exponent(n):
    start = time.time()
    print(n**(n-1))
    end = time.time()
    return (end - start)

n = 10
print(f"the time taken to execution is : {exponent(n)}")
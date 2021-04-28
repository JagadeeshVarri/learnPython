# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years

amount = 10_000
interest = 3.5
years = 7

def value(amount, interest, years):
    val = amount*((1+(0.01*interest)) ** years)
    return round(val, 2)

print(value(amount, interest, years))

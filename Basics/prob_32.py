# Write a Pvalue2thon program to get the least common multiple (LCM) of two positive integers
value1 = int(input("Enter a value : "))
value2 = int(input("Enter another value to get lcm: "))
def lcm(value1,value2):
    if value1>value2:
        greater=value1
    else:
        greater = value2
        
    while True:
        if ((greater%value1==0) and (greater%value2==0)):
            lcm = greater
            break
        greater += 1
    return lcm

print(lcm(value1, value2))

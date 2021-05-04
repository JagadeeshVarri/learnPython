# Program that will return true if the two given integer values are equal or 
# their sum or difference is 5

val1 = int(input("Enter a value : "))
val2 = int(input("Enter a value : "))

def check(val1,val2):
    sum = val1+val2
    dif = val1 - val2
    if val1==val2:
        return True
    elif sum==5 or dif ==5:
        return True
    else:
        return False


print(check(val1, val2))
    
    
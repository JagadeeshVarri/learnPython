# Write a Python program to test whether a passed letter is a vowel or not.

char = input("pass a character to know whether it is vowel are not: ")
vowel = ['a','e','i','o','u']
def isVowel(char):
    for char1 in vowel:
        if char1 == char:
            return True
        else:
            return False

if isVowel(char) == True:
    print(f'{char} is vowel')

else:
    print(f'{char} is constant')
        

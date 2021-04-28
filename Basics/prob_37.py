# Write a Python program to display your details like name, age, address in three different lines

name = input("Enter your name : ")
age = input("Enter your age : ")
address = input("Enter your address : ")

def details(name, age , address):
    print(f"name: {name} \nage: {age} \naddress: {address}")

details(name, age, address)
# Write a Python program to count the number 4 in a given list

def count_4(list1):
    count = 0  
    for num in list1:
        if num == 4:
            count = count + 1

    return count

print(count_4([8, 4, 4, 79, 4, 4]))
print(count_4([8, 4, 2, 4, 7, 4]))
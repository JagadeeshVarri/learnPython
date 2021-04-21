list1 = [1,2,3,"hello",True]
print(list1)
print(type(list1))
print(list1[1:5])
list.append("python")
list.insert(1,"python")

print(list1[-4:-1])

#tuples
tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print(len(tuple1))
x = tuple1.count(5)
print(x)

#sets:

set1 = {"Language", "python", "program"}
print(set1)
print(type(set1))
set1.add("Added")
print(set1)
#dictionary
dict1 = {
  "id": "1",
  "name": "Tom",
  "Age": 26
}
print(dict1)
print(dict1["name"])
dict1["Place"] = "vskp"
print(dict1)

dict1.update({"place": "hyderabad"})
del dict1["Age"]
print(dict1)
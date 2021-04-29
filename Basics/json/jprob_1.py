# Write a Python program to convert JSON data to Python object.

import json
json_obj = '{"name":"vijay","class":"1","age":"6"}'
obj = json.loads(json_obj)
print("Json :")
print("\nName:",obj["name"])
print("\nclass:",obj["class"])
print("\nAge:",obj["age"])
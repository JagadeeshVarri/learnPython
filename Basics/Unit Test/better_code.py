name = ['dsdaf','dsafsar','dsdaf','dsafsar','dsdaf','dsafsar']
name1 = ['dsdaf','dsafsar','dsdaf','dsafsar','dsdaf','dsafsar']

for names, names1 in zip(name, name1):
    print(f'{names} is actually {names1}')

for index, names in enumerate(name, start=1):
    print(f'{names} is actually {index}')
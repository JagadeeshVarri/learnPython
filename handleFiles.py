

#write
file = open('examp.txt','w')
file.write("This is the write command")
file.write("It allows us to write in file")
file.close()

file = open('examp.txt', 'r')

print(file.read())
file.close()

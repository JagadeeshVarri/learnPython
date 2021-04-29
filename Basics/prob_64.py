import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("/home/hanuman/Documents/GitHub/learnPython/Basics/test.txt")))
print("Created: %s" % time.ctime(os.path.getctime("/home/hanuman/Documents/GitHub/learnPython/Basics/test.txt")))

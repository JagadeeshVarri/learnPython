# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)
#sqrt(((x2-x1)**2) + ((y2 - y1)**2))
import math

pt1 = [1,2]
pt2 = [2,1]

dist  = math.sqrt(((pt2[0]-pt1[0])**2) + ((pt2[1] - pt1[1])**2))

print(dist)
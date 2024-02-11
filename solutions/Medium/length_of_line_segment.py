# Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.

import math

def line_length(dot1, dot2):
	return round(math.sqrt((dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2), 2)

print(line_length([15,7], [22,11]))


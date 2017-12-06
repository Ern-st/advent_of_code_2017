#!/usr/bin/env python
input = 368078

boxes = [1]
increment = 1

while boxes[-1] < input:
	increment += 2
	boxes.append(pow(increment, 2))

sideLength = (boxes[-1] - boxes[-2]) / 4

side = boxes[-1]

while side > input:
	side -= sideLength

distance = abs((side + (sideLength/2)) - input )

print "distance = {0}".format( distance + len(boxes) - 1)
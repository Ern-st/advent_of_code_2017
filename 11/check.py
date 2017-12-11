#!/usr/bin/env python
f = open("input.txt")
input = [move.rstrip() for move in f.read().split(",")]

class hex:
	def __init__(self):
		self.coordinates = dict(x=0, y=0, z=0)

	def move(self, direction):
		if direction == "nw":
			self.coordinates['y'] += 1
			self.coordinates['x'] -= 1
		elif direction == "n":
			self.coordinates['y'] += 1
			self.coordinates['z'] -= 1
		elif direction == "ne":
			self.coordinates['x'] += 1
			self.coordinates['z'] -= 1
		elif direction == "se":
			self.coordinates['y'] -= 1
			self.coordinates['x'] += 1
		elif direction == "s":
			self.coordinates['y'] -= 1
			self.coordinates['z'] += 1
		elif direction == "sw":
			self.coordinates['x'] -= 1
			self.coordinates['z'] += 1

	def getCoordinates(self):
		return self.coordinates

	def getDistanceFrom(self, b):
		a = self.coordinates
		distance = (abs(a['x'] - b['x']) + abs(a['y'] - b['y']) + abs(a['z'] - b['z'])) / 2
		# or you could just get the value that is the sum of the other two
		return distance


hexMap = hex()
furthest = 0

for move in input:
	hexMap.move(move)
	distanceTemp = hexMap.getDistanceFrom({'x':0, 'y':0, 'z':0})
	if distanceTemp > furthest:
		furthest = distanceTemp

distance = hexMap.getDistanceFrom({'x':0, 'y':0, 'z':0})
print "solution part 1: {}".format(distance)
print "solution part 2: {}".format(furthest)
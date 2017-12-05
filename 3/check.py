#!/usr/bin/env python
from decimal import *
f = open("input.txt")
input = f.readlines()
f.close()

lines = [sorted([Decimal(s) for s in line.rstrip().split("\t")]) for line in input]
checksum = 0

for numberSet in lines:
	for number in numberSet:
		for modulo in numberSet:
			if (number / modulo) % 1 == 0 and (number / modulo) != 1:
				print "{0} / {1} = {2}".format(number, modulo, number / modulo)
				checksum += (number / modulo)

print "checksum: " + str(checksum)
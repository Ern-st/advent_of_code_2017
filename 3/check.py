#!/usr/bin/env python
f = open("input.txt")
input = f.readlines()
f.close()

lines = [sorted([int(s) for s in line.rstrip().split("\t")]) for line in input]
checksum = 0

for numberSet in lines:
	checksum += (numberSet[-1] - numberSet[0])

print checksum
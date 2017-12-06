#!/usr/bin/env python

input = "0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"

input = [int(m) for m in input.split("\t")]

rounds = 0
prev = []
length = len(input)

while True:
	rounds += 1
	maxValue = max(input)
	maxIndex = input.index(maxValue)
	print "maxIndex: " + str(maxIndex)
	print "input: " + str(input)
	distribute = maxValue
	input[maxIndex] = 0
	while distribute != 0:
		maxIndex += 1
		input[maxIndex % length] += 1
		distribute -= 1
	if input in prev:
		cycles = len(prev) - [i for i,x in enumerate(prev) if x == input][0]
		print "INFINITE LOOP DETECTED!\nRounds used: {0}\nCycles used: {1}".format(rounds, cycles)
		break;
	prev.append(input[:])

#print prev
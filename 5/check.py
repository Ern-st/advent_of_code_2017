#!/usr/bin/env python
f = open("input.txt")
input = [int(jump.rstrip()) for jump in f.readlines()]

def solvePartOne(inputList):
	moves = 0
	index = 0
	while index >= 0 and index < len(inputList):
		value = inputList[index]
		inputList[index] = inputList[index] + 1
		index = index + value
		moves += 1
	print "solution part 1: {}".format(moves)

def solvePartTwo(inputList):
	moves = 0
	index = 0
	while index >= 0 and index < len(inputList):
		value = inputList[index]
		if inputList[index] >= 3:
			inputList[index] -= 1
		else:
			inputList[index] += 1
		index += value
		moves += 1
	print "solution part 2: {}".format(moves)

solvePartOne(input[:])
solvePartTwo(input[:])
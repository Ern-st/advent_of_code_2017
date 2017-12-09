#!/usr/bin/env python
f = open("input.txt")
input = f.read().rstrip()
f.close()

numberList = map(int, list(input))

def solvePartOne(numberList):
	total = 0
	prev = numberList[-1]
	for next in numberList:
		if next == prev:
			total += next
		prev = next

	return "solution part 1: {0}".format(total)

def solvePartTwo(numberList):
	total = 0
	length = len(numberList)
	compare = numberList[(length/2)]
	for index, current in enumerate(numberList):
		compare = numberList[(index + (length/2)) % (length)]
		if current == compare:
			total += current

	return "solution part 2: {0}".format(total)

print solvePartOne(numberList)
print solvePartTwo(numberList)
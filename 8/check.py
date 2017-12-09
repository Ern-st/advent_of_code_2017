#!/usr/bin/env python
f = open("input.txt")
input = [instruction.rstrip() for instruction in f.readlines()]

highscore = 0
registers = {}
for line in input:
	var, action, amount, _, ifVar, ifOperand, ifvalue = line.split(" ")
	if ifVar not in registers.keys():
		registers[ifVar] = 0
	if var not in registers.keys():
		registers[var] = 0
	if eval("registers['" + ifVar + "'] " + ifOperand + " " + ifvalue):
		if action == "inc":
			registers[var] += int(amount)
		elif action == "dec":
			registers[var] -= int(amount)
		highscore = registers[var] if registers[var] > highscore else highscore

_, largestValue = max(registers.items(), key=lambda k: k[1])
print "solution part 1: {}".format(largestValue)
print "solution part 2: {}".format(highscore)
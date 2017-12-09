#!/usr/bin/env python
f = open("input.txt")
input = [int(jump.rstrip()) for jump in f.readlines()]

moves = 0
index = 0
while index >= 0 and index < len(input):
	value = input[index]
	input[index] = input[index] + 1
	index = index + value
	moves += 1
print moves
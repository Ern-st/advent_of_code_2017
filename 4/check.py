#!/usr/bin/env python
f = open("input.txt")
input = f.readlines()

passwordCandidates = [line.rstrip().split(" ") for line in input]
validPasswords = len(passwordCandidates)

print validPasswords

for password in passwordCandidates:
	if len(password) != len(set(password)):
		validPasswords -= 1

print validPasswords
#!/usr/bin/env python
f = open("input.txt")
input = f.readlines()

passwordCandidates = [line.rstrip().split(" ") for line in input]
validPasswords = len(passwordCandidates)

print "part 1: candidates " + str(validPasswords)

for password in passwordCandidates:
	if len(password) != len(set(password)):
		validPasswords -= 1

print "part 1: valid " + str(validPasswords)

validPasswords = len(passwordCandidates)
print "part 2: candidates " + str(validPasswords)

for password in passwordCandidates:
	sortedPassword = [''.join(sorted(word)) for word in password]
	if len(sortedPassword) != len(set(sortedPassword)):
		validPasswords -= 1

print "part 2: valid " + str(validPasswords)

#!/usr/bin/env python
from anytree import Node, RenderTree
import pprint as pp
import collections

class Program(object):
	def __init__(self):
		self.name = None
		self.children = None
		self.weight = None
		self.node = None

	def __str__(self):
	    return str(vars(self))

def programToObject(line):
	p = Program()
	if "->" in line:
		nameAndWeight, children = line.strip().split("->")
		p.children = [child.strip() for child in children.split(",")]
	else:
		nameAndWeight = line.strip()
	p.name = nameAndWeight.split(" ")[0]
	p.weight = nameAndWeight.strip()[nameAndWeight.index("(")+1:nameAndWeight.index(")")]
	return p
	

f = open("input.txt")
input = [programToObject(line) for line in f.readlines()]

nodes = {}

for p in input:
	if p.name not in nodes.keys():
		nodes[p.name] = Node(p.name, weight=p.weight)
	else:
		nodes[p.name].weight = p.weight
	if p.children:
		for child in p.children:
			if child in nodes.keys():
				nodes[child].parent = nodes[p.name]
			else:	
				nodes[child] = Node(child, parent=nodes[p.name])

parent = nodes[nodes.keys()[-1]].ancestors[0]

print "solution part 1: {}".format(parent.name)

def getChildWeight(parent):
	if len(parent.children) == 0:
		return int(parent.weight)
	else:
		weight = 0
		for child in parent.children:
			weight += getChildWeight(child)
		return weight + int(parent.weight)

allResults = []

def recursiveWeightLifter(parent):
	results = []
	parents = {}
	for child in parent.children:
		chWeight = getChildWeight(child)
		parents[chWeight] = child.name 
		results.append(chWeight)
	uniqueWeight = sum([x for x in results if results.count(x)==1])
	allResults.append(results)
	if uniqueWeight != 0:
		uniqueChild = parents[uniqueWeight]
		recursiveWeightLifter(nodes[uniqueChild])
	else:
		siblingsWeight, _ = collections.Counter(allResults[-2]).most_common(1)[0]
		troubleChildWeight = getChildWeight(parent)
		if troubleChildWeight > siblingsWeight:
			solution = int(parent.weight) - abs(troubleChildWeight - siblingsWeight)
		else:
			solution = int(parent.weight) + abs(troubleChildWeight - siblingsWeight)
		print "solution part 2: {}".format(solution)

		for pre, fill, node in RenderTree(parent):
			print("%s%s %s" % (pre.encode('utf-8'), node.name.encode('utf-8'), node.weight))

recursiveWeightLifter(parent)
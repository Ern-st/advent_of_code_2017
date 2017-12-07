#!/usr/bin/env python
from anytree import Node, RenderTree
import pprint as pp

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
		nodes[p.name] = Node(p.name)
	if p.children:
		for child in p.children:
			if child in nodes.keys():
				nodes[child].parent = nodes[p.name]
			else:	
				nodes[child] = Node(child, parent=nodes[p.name])

parent = nodes[nodes.keys()[-1]].ancestors[0]

for pre, fill, node in RenderTree(parent):
    print("%s%s" % (pre.encode('utf-8'), node.name.encode('utf-8')))
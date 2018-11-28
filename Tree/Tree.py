#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : Tree.py
@Date  : 2018/11/28
@Desc  : 
"""

import copy
from DataStructure.DrawData.DrawTree import DrawTree

class Node:
	def __init__(self, label=None, value=None):
		self.value = value
		self.label = label
		self.child = []

class Tree:
	def __init__(self):
		self.root = None
		self.length = 0
		self._traversePath = list()
		self._path = None

	def __repr__(self):
		print(self.levelOrder(self.root))
		return "<type: %s, size: %d>\n" % (self.__class__.__name__, self.length)

	def addRoot(self, label, value):
		self.root = Node(label, value)
		self.length += 1

	def addChild(self, root, fatherLabel, child):
		if root and root.label == fatherLabel:
			root.child.append(Node(child[0], child[1]))
			self.length += 1
			return True
		elif root:
			for childNode in root.child:
				self.addChild(childNode, fatherLabel, child)
		return False

	def addChildren(self, root:Node, fatherLabel, *args):
		if root and root.label == fatherLabel:
			for label, value in args:
				root.child.append(Node(label, value))
				self.length += 1
			return True
		elif root:
			for childNode in root.child:
				self.addChildren(childNode, fatherLabel, *args)
		return False

	def levelOrder(self, root):
		# 用列表模拟栈，实现广度搜索
		queue = []
		queue.append(root)
		while len(queue) > 0:
			popNode = queue.pop(0)
			self._traversePath.append(popNode)
			for item in popNode.child:
				queue.append(item)

		self._path = [{item.label: item.value} for item in self._traversePath]
		return self._path


if __name__ == "__main__":
	T = Tree()
	T.addRoot('A', 1)
	T.addChild(T.root, 'A', ('B', 2))
	T.addChildren(T.root, 'B', ('C', 3), ('D', 4))
	T.addChild(T.root, 'A', ('E', 2))
	T.addChild(T.root, 'A', ('F', 2))
	print(T)
	img = DrawTree(T.root, filename=T.__class__.__name__, directory='output')
	img.draw()
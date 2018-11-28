#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : BinaryTree.py
@Date  : 2018/11/28
@Desc  : 
"""
import copy
from DataStructure.DrawData import DrawTree


class Node:
	def __init__(self, value=None):
		self.value = value
		self.label = None
		self.left = None
		self.right = None


class BinaryTree():
	def __init__(self):
		self.root = None
		self.length = 0
		self.label = 'A'
		self.Traversal = None
		self.path = None

	def __repr__(self):
		self.levelOrder(self.root)
		print(self.path)
		return "<type: %s, size: %d>\n" % (self.__class__.__name__, self.length)

	def addRoot(self, value):
		self.root = Node(value)
		self.root.label = chr(ord(self.label) + self.length)
		self.length += 1
		self.levelOrder(self.root)

	def addLeft(self, root: Node, fatherLabel, value):
		if root and root.label == fatherLabel:
			root.left = Node(value)
			root.left.label = chr(ord(self.label) + self.length)
			self.length += 1
			self.levelOrder(self.root)
			return True
		elif root:
			self.addLeft(root.left, fatherLabel, value)
			self.addLeft(root.right, fatherLabel, value)
		return False

	def addRight(self, root: Node, fatherLabel, value):
		if root and root.label == fatherLabel:
			root.right = Node(value)
			root.right.label = chr(ord(self.label) + self.length)
			self.length += 1
			self.levelOrder(self.root)
			return True
		elif root:
			self.addRight(root.left, fatherLabel, value)
			self.addRight(root.right, fatherLabel, value)
		return False

	def levelOrder(self, root):
		traversal = []
		# 用列表模拟栈，实现广度搜索
		queue = []
		queue.append(root)
		while len(queue) > 0:
			popNode = queue.pop(0)
			if popNode.left:
				queue.append(popNode.left)
			if popNode.right:
				queue.append(popNode.right)
			traversal.append(popNode)
		self.Traversal = traversal
		self.path = [{item.label: item.value} for item in self.Traversal]


class Traversal(object):
	def __init__(self):
		self.traversePath = list()

	def preOrder(self, root):
		if root:
			self.traversePath.append(root)
			self.preOrder(root.left)
			self.preOrder(root.right)

	def inOrder(self, root):
		if root:
			self.inOrder(root.left)
			self.traversePath.append(root)
			self.inOrder(root.right)

	def postOrder(self, root):
		if root:
			self.postOrder(root.left)
			self.postOrder(root.right)
			self.traversePath.append(root)

	def levelOrder(self, root):
		# 用列表模拟栈，实现广度搜索
		queue = []
		queue.append(root)
		while len(queue) > 0:
			popNode = queue.pop(0)
			if popNode.left:
				queue.append(popNode.left)
			if popNode.right:
				queue.append(popNode.right)
			self.traversePath.append(popNode)


if __name__ == "__main__":
	bT = BinaryTree()
	bT.addRoot(1)
	bT.addLeft(bT.root, 'A', 2)
	bT.addRight(bT.root, 'A', 3)
	bT.addLeft(bT.root, 'B', 4)
	bT.addRight(bT.root, 'B', 5)
	bT.addLeft(bT.root, 'C', 6)
	bT.addRight(bT.root, 'C', 7)
	print(bT)
	p = [{item.label: item.value} for item in bT.path]
	# p[0]
	img = DrawTree.DrawBinaryTree(p, filename=bT.__class__.__name__, directory='imgOutput')
	img.draw()
	print(bT.path)
	print(bT)

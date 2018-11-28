#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : DrawTree.py
@Date  : 2018/11/28
@Desc  : 
"""
from DataStructure.DrawData.DrawHeap import DrawHeap
from graphviz import Digraph
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
class DrawBinaryTree(DrawHeap):
	pass

class DrawTree:
	def __init__(self, root, filename=None, directory=None, cleanup=False):
		self.root = root
		self.source = None
		self.imgAddress = None
		self.filename = filename
		self.directory = directory
		self.cleanup = cleanup

	def draw(self):
		dot = Digraph(comment='The Tree')
		# 用列表模拟栈，实现广度搜索
		queue = []
		queue.append(self.root)
		dot.node(queue[0].label, (queue[0].label + ':' + str(queue[0].value)))
		while len(queue) > 0:
			popNode = queue.pop(0)
			for childNode in popNode.child:
				value = "%s:%d" %(childNode.label, childNode.value)
				dot.node(childNode.label, value)
				dot.edge(popNode.label, childNode.label)
				queue.append(childNode)
		self.source = dot.source
		self.imgAddress = dot.render(filename=self.filename, directory=self.directory, view=False, cleanup=self.cleanup,
		                             format='png')
		img = mpimg.imread(self.imgAddress)
		plt.imshow(img)
		plt.axis('off')
		plt.show()


if __name__ == "__main__":
	pass
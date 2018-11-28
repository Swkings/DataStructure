#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : DrawHeap.py
@Date  : 2018/11/27
@Desc  : 
"""
from graphviz import Digraph
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
class DrawHeap:
	def __init__(self, heap, filename=None, directory=None, cleanup=False):
		self.heap = heap
		self.source = None
		self.imgAddress = None
		self.filename = filename
		self.directory = directory
		self.cleanup = cleanup

	def draw(self):
		dot = Digraph(comment='The Heap')
		for i in range(len(self.heap)):
			dot.node('->'+str(i), str(self.heap[i]))
		for i in range(math.floor(len(self.heap) / 2)):
			left, right = i * 2 + 1, i * 2 + 2
			dot.edge('->'+str(i), '->'+str(left))
			if right < len(self.heap):
				dot.edge('->' + str(i), '->' + str(right))
		# # 创建一堆边，即连接AB的两条边，连接AC的一条边。
		# dot.edges(['AB', 'AC', 'AB'])
		# # dot.view()
		#
		# # 在创建两圆点之间创建一条边
		# dot.edge('B', 'C', 'test')
		# # dot.view()

		# 获取DOT source源码的字符串形式
		self.source = dot.source

		# 保存source到文件，并提供Graphviz引擎

		self.imgAddress = dot.render(filename=self.filename, directory=self.directory, view=False, cleanup=self.cleanup, format='png')
		img = mpimg.imread(self.imgAddress)
		plt.imshow(img)
		plt.axis('off')
		plt.show()

if __name__ == "__main__":
	heap = [7, 5, 6, 4, 2, 1, 3]
	gra = DrawHeap(heap, filename=DrawHeap.__class__.__name__, directory='output')
	gra.draw()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : Heap.py
@Date  : 2018/11/27
@Desc  : 
"""
import math
import copy
from DataStructure.DrawData.DrawHeap import DrawHeap
class MaxHeap:
	def __init__(self, array=None):
		# 深拷贝，防止继承后对同一个数组操作
		self.heap = copy.deepcopy(array)
		if self.heap:
			self.heap = self._adjust(self.heap)
		else:
			self.heap = []

	def __repr__(self):
		print(self.heap)
		return "<type: %s, size: %d>\n" % (self.__class__.__name__, len(self.heap))

	def _sink(self, array, index):
		left, right = index * 2 + 1, index * 2 + 2
		sinkIndex = left
		if right < len(array):
			if array[left] > array[right]:
				sinkIndex = left
			else:
				sinkIndex = right
		if sinkIndex < len(array) and array[sinkIndex] > array[index]:
			array[index], array[sinkIndex] = array[sinkIndex], array[index]
			self._sink(array, sinkIndex)

	def _swim(self, array, index):
		if index != 0:
			fatherNode = math.floor((index-1)/2)
			if array[index] > array[fatherNode]:
				array[fatherNode], array[index] = array[index], array[fatherNode]
				self._swim(array, fatherNode)

	def _adjust(self, array):
		for i in range(math.floor(len(array)/2), -1, -1):
			self._sink(array, i)
		return array

	def push(self, value):
		self.heap.append(value)
		self._swim(self.heap, len(self.heap)-1)

	def pop(self):
		# 先交换，再pop出最后一个元素，然后调整
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		value = self.heap.pop()
		self._sink(self.heap, 0)
		return value

class MinHeap(MaxHeap):
	# def __init__(self, array=None):
	# 	if array:
	# 		self.heap = self._adjust(array)
	# 	else:
	# 		self.heap = []

	def _sink(self, array, index):
		left, right = index * 2 + 1, index * 2 + 2
		sinkIndex = left
		if right < len(array):
			if array[left] < array[right]:
				sinkIndex = left
			else:
				sinkIndex = right
		if sinkIndex < len(array) and array[sinkIndex] < array[index]:
			array[index], array[sinkIndex] = array[sinkIndex], array[index]
			self._sink(array, sinkIndex)

	def _swim(self, array, index):
		if index != 0:
			fatherNode = math.floor((index-1)/2)
			if array[index] < array[fatherNode]:
				array[fatherNode], array[index] = array[index], array[fatherNode]
				self._swim(array, fatherNode)

if __name__ == '__main__':
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	minHeap = MinHeap(array)
	maxHeap = MaxHeap(array)
	print(minHeap)
	img1 = DrawHeap(minHeap.heap, filename=minHeap.__class__.__name__, directory='imgOutput')
	img1.draw()
	img2 = DrawHeap(maxHeap.heap, filename=maxHeap.__class__.__name__, directory='imgOutput')
	img2.draw()




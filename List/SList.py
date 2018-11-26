#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : SList.py
@Date  : 2018/11/25
@Desc  : 单向链表, index从1开始
"""

import copy
class Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class SLinkList:
	def __init__(self):
		self.head = Node(None)  # 初始化一个头结点
		self.end = self.head  # 记录尾结点，方便添加元素
		self.length = 0

	def __repr__(self):
		self.print()
		return "<class: %s, size: %d>" % (self.__class__.__name__, self.length)

	def print(self):
		print("head", end=' ')
		pNode = self.head.next
		while pNode:
			print("->", end=' ')
			print(pNode.value, end=' ')
			pNode = pNode.next
		print("\n")

	def create(self, value):
		node = Node(value)
		self.end.next = node
		# self.end = self.end.next
		self.end = node
		self.length += 1
		return True

	def isEmpty(self):
		if self.length == 0:
			return True
		return False

	def getElem(self, index):
		if self.isEmpty():
			raise IndexError("SLinkList is empty.")
		elif 0 < index <= self.length:
			pNode = self.head
			pIndex = 0
			while pIndex < index and pNode:
				pNode = pNode.next
				pIndex += 1
			return pNode.value
		else:
			raise IndexError("Index is out of range.")


	def insert(self, index, elem):
		node = Node(elem)
		self.length += 1  # 先加1，保证能加在最后位置
		if self.isEmpty() and index == 1:
			self.head.next = node
		else:
			if 0 < index <= self.length:
				pNode = self.head
				pIndex = 0
				while pIndex < index-1 and pNode:
					pNode = pNode.next
					pIndex += 1
				temp = pNode.next
				pNode.next = node
				node.next = temp
				if index == self.length:
					self.end.next = node
					self.end = self.end.next
			else:
				self.length -= 1  # 出错减1
				raise IndexError("Index is out of range.")

	def delete(self, index):
		if 0 < index <= self.length:
			pNode = self.head
			pIndex = 0
			while pIndex < index-1 and pNode:
				pNode = pNode.next
				pIndex += 1
			pNode.next = pNode.next.next
			if index == self.length:
				self.end.next = pNode
				self.end = self.end.next
			self.length -= 1
		else:
			raise IndexError("Index is out of range.")

	def reverse(self):
		"""链表的基本形式是：1 -> 2 -> 3 -> null，反转需要变为 3 -> 2 -> 1 -> null"""
		nextList = None
		pNode = self.head.next
		self.end = pNode
		while pNode:
			temp = pNode.next
			pNode.next = nextList
			nextList = pNode
			pNode = temp
		self.head.next = nextList




if __name__ == "__main__":
	sList = SLinkList()
	sList.create(1)
	sList.create(2)
	sList.print()
	sList.insert(3, 3)
	sList.print()
	sList.create(4)
	sList.print()
	sList.delete(4)
	sList.print()
	sList.create(4)
	sList.print()
	sList.reverse()
	sList.print()
	sList.create(5)
	sList.print()
	print(sList)

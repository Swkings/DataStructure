#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : DList.py
@Date  : 2018/11/25
@Desc  : 双向链表
"""


class Node:
	def __init__(self, value=None):
		self.value = value
		self.prev = None
		self.next = None

class DLinkList:
	def __init__(self):
		self.head = Node(None)  # 初始化一个头结点
		self.end = self.head  # 记录尾结点，方便添加元素
		self.length = 0

	def __repr__(self):
		self.print()
		return "<class: %s, size: %d>\n" % (self.__class__.__name__, self.length)

	def print(self, reverse=False):
		if not reverse:
			print("head", end=' ')
			pNode = self.head.next
			while pNode:
				print("->", end=' ')
				print(pNode.value, end=' ')
				pNode = pNode.next
			print("\n", end='')
		else:
			print("end", end=' ')
			pNode = self.end
			while pNode:
				print("->", end=' ')
				print(pNode.value, end=' ')
				pNode = pNode.prev
			print("\n", end='')

	def create(self, value):
		node = Node(value)
		self.end.next = node
		node.prev = self.end
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
		if 0 < index <= self.length:
			pNode = self.head
			pIndex = 0
			while pIndex < index-1 and pNode:
				pNode = pNode.next
				pIndex += 1
			temp = pNode.next
			pNode.next = node
			node.prev = pNode
			node.next = temp

			if index == self.length:
				self.end.next = node
				self.end = self.end.next
			else:
				# 结点插在最后时，temp为None，没有prev属性
				temp.prev = node
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
			else:
				# 删除最后一个结点后pNode.next指向None，没有prev属性
				pNode.next.prev = pNode
			self.length -= 1
		else:
			raise IndexError("Index is out of range.")


if __name__ == "__main__":
	dList = DLinkList()
	dList.create(1)
	dList.insert(2, 2)
	print(dList.getElem(2))
	print(dList)
	dList.insert(3, 3)
	print(dList)
	dList.delete(3)
	print(dList)
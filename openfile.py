#coding:utf-8
#gracehappy # grace@zju.edu.cn # lint@esrichina-bj.cn
import os
import time


class Bucket:
	"""docstirng for Bucket"""
	def __init__(self, size):
		if not isinstance(size, int):
			raise TypeError('size should be a integer')
		elif size <= 0:
			raise ValueError('size should be a positive integer')
		self.__size = size
		self.__bucket = [None] * self.__size
		self.setHashFunction()
	def getsize():
		return self.__size
	size = property(getsize)
	def setHashFunction(self, func = hash):
		self.hashFunc = func
	def insert(self, obj):
		index = self.hashFunc(obj) % self.__size
		bucketCell = self.__bucket[index]
		if bucketCell == None:
			self.__bucket[index] = [self.Node(obj)]
			return True
		if obj in bucketCell:
			innerindex = bucketCell.index(obj)
			bucketCell[innerindex].add()
			return True
		else:
			bucketCell.append(self.Node(obj))
			return True
	def delete(self, obj):
		index = self.hashFunc(obj) % self.__size
		bucketCell = self.__bucket[index]
		if bucketCell == None:
			return False
		else:
			for node in bucketCell:
				if node.getElement() == obj:
					if node.dec() == False:
						del node
					break
			else:
				return False
			return True
	def find(self, obj):
		index = self.hashFunc(obj) % self.__size
		bucketCell = self.__bucket[index]
		if bucketCell == None:
			return False
		else:
			for node in bucketCell:
				if node.getElement() == obj:
					return True
			else:
				return False
	def findbyindex(self, bucketindex, innerindex):
		if not isinstance(bucketindex, int) or isinstance(innerindex, int):
			raise TypeError
		if bucketindex < 0 or bucketindex >= self.__size:
			raise ValueError
		bucketCell = self.__bucket[bucketindex]
		if innerindex < 0 or innerindex >= len(bucketCell):
			raise ValueError
		else:
			return bucketCell[innerindex].getElement()
	def getBucket(self):
		res = []
		n  = 0
		for bucketCell in self.__bucket:
			if bucketCell == None:
				continue
			n+=1
			for node in bucketCell:
				resnode = [node.getElement(), node.getNumber()]
				res.append(resnode)
		return res 
	def diagram(self):
		noneNum = 0
		totalNum = self.__size
		for idx, bucketCell in enumerate(self.__bucket):
			if bucketCell == None:
				noneNum += 1
	class Node:
		def __init__(self, element):
			self.__element = element
			self.__number = 1
		def add(self):
			self.__number += 1
		def dec(self):
			self.__number -= 1
			if self.__number == 0:
				return False
		def getNumber(self):
			return self.__number
		def getElement(self):
			return self.__element
class ConflictException(Exception):
	def __init__(self, reason):
		Exception.__init__(self)
		self.reason = reason


def main(*args, **kw):
	fp = open('www.csdn.net.sql','r')
	passwords = []
	count = []
	print 'reading...'
	fp.seek(0,2)
	totalbyte = fp.tell()
	fp.seek(0,0)
	n = 0
	totalStart = time.time()
	insertCost = 0
	bucket = Bucket(10000)
	line = fp.readline()
	while line != '':
		n += 1
		if n % 10000 == 0:
			print '%.4s%%' %(float(fp.tell()) / totalbyte * 100)
			
			totalCost = time.time() - totalStart
			print 'insertCost = %.4s%%' %(float(insertCost) / totalCost * 100)
			totalStart = time.time()
			insertCost = 0
		password = line.split('#')[1].strip()
		insertStart = time.time()
		bucket.insert(password)
		insertCost += time.time() - insertStart
		line = fp.readline()
	fp.close()
	fp = open('csdn.password','w')
	print 'writing...'
	for line in bucket.getBucket():
		fp.write('%s # %s\n' %(line[0], line[1]))
	fp.close()
if __name__ == '__main__':
	main()
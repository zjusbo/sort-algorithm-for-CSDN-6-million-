#coding:utf-8
#gracehappy # grace@zju.edu.cn # lint@esrichina-bj.cn
import os
import time
class DicTree(object):
	"""docstring for DicTree"""
	def __init__(self, arg):
		super(DicTree, self).__init__()
		self.arg = arg
		

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
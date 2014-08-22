#coding:utf-8
#gracehappy # grace@zju.edu.cn # lint@esrichina-bj.cn
import os
import time
import threading
class thread(threading.Thread):
	def __init__(self, threadid, fp, fplock, startline, endline, ofp):
		threading.Thread.__init__(self)
		self.startline = startline
		self.endline = endline
		self.id = threadid
		self.fp = fp
		self.fplock = fplock
		self.ofp = ofp
	def run(self):
		n = 0
		while n < self.startline:
			self.fp.readline()
			n+=1
		self.currentline = self.startline
		self.passwords = []
		while self.currentline <= self.endline:
			if self.currentline % 10000 == 0:
				print '[%s] %s' %(self.id, self.currentline)
			line = self.fp.readline()
			if len(line.split(' # ')) < 2:
				self.currentline += 1
				continue
			password = line.split(' # ')[1].strip()
			self.insert(password)
			self.currentline += 1
		for password in self.passwords:
			self.ofp.write('%s # %s\n' %(password[0], password[1]))
		print 'thread %s finish' %self.id
	def insert(self, item):
		if len(self.passwords) == 0:
			self.passwords.append([item, 1])
		else:
			self.__insert(item, 0, len(self.passwords)-1)
	def __insert(self, item, start, end):
		if start == end:
			if self.compare(item, self.passwords[start][0]) == 0:
				self.passwords[start][1] += 1
			elif self.compare(item, self.passwords[start][0]) > 0:
				self.passwords.insert(start+1,[item, 1])
			else:
				self.passwords.insert(start, [item, 1])
		else:
			mid = (end + start) / 2
			if self.compare(item, self.passwords[mid][0]) == 0:
				self.passwords[mid][1] += 1
			elif self.compare(item, self.passwords[mid][0]) > 0:
				self.__insert(item, mid+1, end)
			else:
				self.__insert(item, start, mid)
	def compare(self, a,b):
		for idx, ca in enumerate(a):
			if idx == len(b):# a is longer than b
				return 1
			elif ord(ca) > ord(b[idx]):
				return 1
			elif ord(ca) < ord(b[idx]):
				return -1
		if len(a) == len(b):
			return 0
		else:
			return -1 #b is longer than a 
def splitsort(*args, **kw):
	n = 6428633
	# while line != '':
	# 	n+=1
	# 	line = fp.readline()
	print 'total line %s' %n

	fplock = threading.Lock()
	ofp = []
	threads=[]
	last = 0
	partitionLen = 300000
	for  i in xrange(0,n / partitionLen+1):
		fp = open('www.csdn.net.sql','r')
		endline = (i+1) * partitionLen - 1
		if endline > n:
			endline = n-1
		ofp.append(open('res%s-%s' %(i*partitionLen,endline),'w')) 
		t = thread(i, fp, fplock, i * partitionLen, endline, ofp[-1])
		threads.append(t)
	for t in threads:
		t.start()
	for idx, t in enumerate(threads):
		t.join()
		ofp[idx].close()
class merge:
	def __init__(self, fps, ofp):
		self.fps = fps
		self.ofp = ofp
		self.fpslen = len(fps)
	def start(self):
		items = []
		for fp in self.fps[:]:
			line = fp.readline()
			if line == '':
				self.fps.remove(fp)
				self.fpslen -= 1
			else:
				items.append(line.split(' # '))
		#for len(fps) > 0
		n = 0
		while self.fpslen > 0:
			n += 1
			#find least items
			if n % 10000 == 0:
				print '%s items merged' %n
			leastitem = []
			for item in items:
				if len(leastitem) == 0:
					leastitem = [item[0],int(item[1])]
				elif self.compare(item[0],leastitem[0]) < 0:
					leastitem = [item[0],int(item[1])]
				elif self.compare(item[0],leastitem[0]) == 0:
					leastitem[1] += int(item[1])
			#merge least items
			#insert least items
			self.ofp.write('%s # %s\n' %(leastitem[0],leastitem[1]))
			#update items
			removefp = []
			removeidx = []
			lastidx = 0
			for idx, item in enumerate(items):
				if item[0] == leastitem[0]:
					line = self.fps[idx].readline()
					if line == '':
						removefp.append(self.fps[idx])
						removeidx.append(idx)
					else:
						items[idx] = line.split(' # ')
			for fp in removefp:
				self.fps.remove(fp)
				self.fpslen -= 1
			length = 0
			for idx in removeidx:
				items.pop(idx-length)
				length += 1
	def compare(self, a,b):
		for idx, ca in enumerate(a):
			if idx == len(b):# a is longer than b
				return 1
			elif ord(ca) > ord(b[idx]):
				return 1
			elif ord(ca) < ord(b[idx]):
				return -1
		if len(a) == len(b):
			return 0
		else:
			return -1 #b is longer than a 
def test():
	files = os.listdir(os.getcwd())
	for filename in files[:]:
		if len(filename.split('.')) > 1:
			files.remove(filename)
	fps = []
	print files
	for filename in files:
		fps.append(open(filename, 'r'))
	ofp = open('res.txt','w')
	m = merge(fps[:],ofp)
	m.start()
	for fp in fps:
		fp.close()
	ofp.close()
if __name__ == '__main__':
	test()


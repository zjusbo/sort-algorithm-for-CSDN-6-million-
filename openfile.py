#coding:utf-8
#gracehappy # grace@zju.edu.cn # lint@esrichina-bj.cn
import os
import time
import threading
class thread(threading.Thread):
	def __init__(self, threadid, fp, fplock, startline, endline, ofp):
		self.startline = startline
		sef.endline = endline
		self.id = threadid
		self.fp = fp
		self.fplock = fplock
		self.ofp = ofp
	def run(self):
		self.currentline = self.startline
		self.passwords = []
		while self.currentline <= self.endline:
			self.fplock.accquire()
			line = fp.readline()
			self.fplock.release()
			password = line.split(' # ')[1].strip()
			self.insert(password)
		self.currentline += 1
		for password in passwords:
			ofp.write(password[0] + '#' + password[1] + '\n')
	def insert(self, item):
		self.__insert(item, 0, len(self.passwords))
	def __insert(self, item, start, end):
		if start == end:
			if self.compare(item, self.passwords[start][0]) == 0:
				self.passwords[start][1] += 1
			elif self.compare(item, self.passwords[start][0]) > 0:
				self.passwords.insert(start+1,[item, 1])
			else:
				self.passwords.insert(start, [item 1])
		else:
			mid = (end - start) / 2
			if self.compare(item, self.passwords[mid][0]) == 0:
				self.passwords[mid][1] += 1
			elif self.compare(item, self.passwords[mid][0]) > 0:
				self.__insert(self, item, mid+1, end)
			else:
				self.__insert(self, item, start, mid-1)
	def compare(self, a,b):
		for idx, ca in enumerate(a):
			if idx == len(b):# a is longer than b
				return 1
			elif ord(ca) > ord(b[idx]):
				return 1
			elif ord(ca) < ord(b[idx]):
				return -1
			else:
				return 0
		return -1 #b is longer than a 
def main(*args, **kw):
	fp = open('www.csdn.net.sql','r')
	line = fp.readline()
	n = 1
	while line != '':
		n+=1
		line = fp.readline()
	fp.seek(0,0)
	print 'total line %s' %n

	fplock = threading.Lock()
	thread(0, fp, fplock, 0, n)
	thread.start()
	thread.join()
	
if __name__ == '__main__':
	main()
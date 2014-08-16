#coding:utf-8
#gracehappy # grace@zju.edu.cn # lint@esrichina-bj.cn
import os
import time


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
		if password not in passwords:
			passwords.append(password)
			count.append(1)
		else:
			i = passwords.index(password)
			count[i] += 1
		insertCost += time.time() - insertStart
		line = fp.readline()
	fp.close()
	fp = open('csdn.password','w')
	print 'writing...'
	for idx, line in enumerate(passwords):
		fp.write('%s # %s\n' %(line, count[idx]))
	fp.close()
if __name__ == '__main__':
	main()
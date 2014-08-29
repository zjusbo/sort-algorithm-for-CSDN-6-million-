#coding:utf-8
#gracehappy # grace@zju.edu.cn # lint@esrichina-bj.cn
import os
import time
import threading

maxlenth = 100000
def run():
	fp = open('res.txt','r')
	res = []
	line = fp.readline()
	n = 0
	while line != '':
		if n % 10000 == 0:
			print n
		item = line.split(' # ')
		if len(res) == 0:
			res.append([item[0], int(item[1])])
		else:
			insert(item[0],int(item[1]),res)
		line = fp.readline()
		n += 1
	ofp = open('finalres.txt','w')
	for item in res:
		ofp.write('%s # %.6s%%\n' %(item[0], float(item[1]) / 6428633 * 100))
	ofp.close()
	fp.close()
def insert(item,time, res):
	length = len(res)
	__insert(item, time, res, 0, length)
def __insert(item, time, res, start, end):
	if start == end:
		if start == len(res):
			return
		elif time > res[start][1]:
			res.insert(start, [item,time])
		else:
			res.insert(start+1, [item,time])
		if len(res) > maxlenth:
			res.pop(-1)
	else:
		mid = (start + end) / 2
		if time > res[mid][1]:
			__insert(item, time, res, start,mid)
		elif time < res[mid][1]:
			__insert(item, time, res, mid+1, end)
		else:
			__insert(item, time, res, mid, mid) 

def main():
	run()
if __name__ == '__main__':
	run()


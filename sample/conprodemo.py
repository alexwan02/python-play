#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time 
from coroutine import coroutine

def consumer():
	p = ''
	while True:
		n = yield p
		if not n:
			return
		print '[CONSUMER ] consumer %s...' % n
		time.sleep(1)
		p = '200 OK : %s' % n
		
		

def producer(c):
	c.next()
	n = 0
	while n < 5:
		n = n +1
		print '[PRODUCER] producing %s...' % n
		r = c.send(n)
		print '[PRODUCER] Consumer return: %s' % r

	c.close()

def follow(file):
	file.seek(0 , 2)
	while True:
		line = file.readline()
		if not line:
			time.sleep(0.1)
			continue
		yield line


@coroutine
def grep(pattern , tartget):
	# for line in lines:
	# 	if pattern in line:
	# 		yield line
	print 'Looking for %s' % pattern
	try:
		while True:
			line = (yield)
			if pattern in line:
				tartget.send(line)
	except GeneratorExit:
		print 'Going away. Goodbye'

@coroutine
def countdown(n):
	print 'Counting down from %s' % n
	while n >=0:
		newvalue = (yield n)
		# If a new value got sent in , reset n with it
		if newvalue is not None:
			n = newvalue
		else:
			n -= 1


@coroutine
def filter(tartget):
	while True:
		item = (yield)

		# 
		tartget.send(item)



# Set up a processing pipe : tail -f | grep python 

if __name__ == '__main__':
	# c = consumer()

	# producer(c)
	# with open('text' , 'r') as file:
	# 	f = follow(file)
	# 	hlines= grep("python",f)
	# 	for line in hlines:
	# 		print line
	c = countdown(5)
	print c
	print c.next()
	print c.next()
	# for n in c:
	# 	print n
	# 	if n == 5:
	# 		c.send(3)







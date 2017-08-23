#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re 

if __name__ == '__main__':
	print re.match(r'^\d{3}\-\d{3 , 8}$' , '010-12345')

	test = '用户输入的字符串'
	if re.match(r'正则表达式' , test):
		print 'ok'
	else:
		print 'failed'

	# split
	print re.split(r'\s+' , 'a b    c')

	print re.split(r'[\s\,\;]+' , 'a,b;; c   d')

	# group
	g = re.match(r'^(\d{3})-(\d{3,8})$' , '010-12345').groups()

	for i in g:
		print i
	# 非贪婪匹配
	g1 = re.match(r'^(\d+?)(0*)$' , '1023000').groups()

	for x in g1:
		print x

	# 正则预编译
	re_telphone = re.compile(r'^(\d{3})\-(\d{3,8})$')
	print re_telphone.match('010-12345').groups()

	


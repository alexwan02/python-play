#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import itertools
#count
natuals = itertools.count(1)
# for n in natuals:
# 	if n > 100:
# 		break
# 	print n
# cycle
cs = itertools.cycle('ABC')

#repeat
ns = itertools.repeat('A' , 10)

# for n in ns:
# 	print n

# takewhile
ns = itertools.takewhile(lambda x: x <= 200 , natuals)

# for n in ns:
# 	print n

#chain
for c in itertools.chain('ABC' , 'XYZ'):
	print c

# groupby
for key , group in itertools.groupby('AAABBBCCCAA'):
	print key , list(group)

for key , group in itertools.groupby('AaaBbbbCccCAaA' , lambda c: c.upper()):
	print key , list(group)

# imap
for x in itertools.imap(lambda x , y : x * y , [10 , 20 , 30 ] , itertools.count(1)):
	print x

# imap 懒加载
# r = itertools.imap(lambda x : x * x , itertools.count(1))
r = map(lambda x: x * x , itertools.count(1))
for n in itertools.takewhile(lambda x : x < 100 , r):
	print n

# ifilter() 


















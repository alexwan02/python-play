#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from collections import namedtuple , deque , defaultdict
from collections import OrderedDict , Counter

# namedtuple
Point = namedtuple('Point' , ['x' , 'y'])
p = Point(1 , 2)
print p

# deque
q = deque(['a' , 'b' , 'c'])
q.append('x')
q.appendleft('y')
print q

# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

print dd['key1'] , dd['key2']

# ordered dit

print OrderedDict([('a' , 1) , ('b' , 2) , ('c' , 3)])

class LastUpdateOrderedDict(OrderedDict):
	def __init__(self , capacity):
		super(LastUpdateOrderedDict , self).__init__()
		self._capacity = capacity

	def __setitem__(self , key , value):
		containsKey = 1 if key in self else 0

		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last = False)
			print 'remove: ' , last

		if containsKey:
			del self[key]
			print 'set:' , (key , value)

		else:
			print 'add:' , (key , value)

		OrderedDict.__setitem__(self , key , value)

# Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1

print c




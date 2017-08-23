#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import base64
print 'encode = ' , base64.b64encode('binary\x00string')
s = base64.b64encode('binary\x00string')
print 'decode = '  , base64.b64decode('YmluYXJ5AHN0cmluZw==')


s = 'YWJjZA'

for i in range(4 - len(s) % 4):
	s += '='

print 'decode = ' , base64.b64decode(s)
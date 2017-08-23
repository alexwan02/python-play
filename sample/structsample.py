#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import struct

print r'%s' % struct.pack('>I' , 10240099)

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

print chr((10240099 & 0xff000000) >> 24)
print chr((10240099 & 0xff0000) >> 16)
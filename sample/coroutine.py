#!/usr/bin/env python
# -*- coding: utf-8 -*- 
def coroutine(func):
	def start(*args , **kwargs):
		cr = func(*args , **kwargs)
		cr.next()
		return cr
	return start

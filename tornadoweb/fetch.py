#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from tornado.httpclient import HTTPClient , AsyncHTTPClient
from tornado.concurrent import Future

import time

def synchronous_fetch(url):
	http_client = HTTPClient()
	response = http_client.fetch(url)
	return response.body

def handle_response(response):
	print 'response = ' , response.body
	if response.error:
		print 'Error: %s' % response.error
	else:
		print 'Result: %s' % response.body

def asynchronous_fetch(url , callback):
	http_client = AsyncHTTPClient()
	http_client.fetch(url , callback)



def async_fetch_future(url):
	http_client = AsyncHTTPClient()
	my_future = Future()
	fetch_future = http_client.fetch(url)
	fetch_future.add_done_callback(lambda f : my_future.set_result(f.result()))
	return my_future


# print synchronous_fetch(r'http://localhost:8888/')

asynchronous_fetch(r'http://localhost:8888/' , handle_response)
# print async_fetch_future(r'http://localhost:8888/').result(5)
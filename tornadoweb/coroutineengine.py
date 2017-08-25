#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from tornado import gen
from tornado.httpclient import HTTPClient , AsyncHTTPClient
from tornado.ioloop import IOLoop

@gen.coroutine
def fetch_coroutine(url):
	http_client = AsyncHTTPClient()
	response = yield http_client.fetch(url)
	# print 'response = ' , response
	raise gen.Return(response)



# thread_pool = ThreadPoolExecutor(4)


# print thread_pool.submit(fetch_coroutine , r"http://localhost:8888/")

# def produce():
# 	fetch = fetch_coroutine(r"http://localhost:8888/")
# 	def handle_response(f):
# 		print f.result
# 	fetch.add_done_callback(handle_response)


def grep(pattern):
	print 'Searching for : ' , pattern
	while True:
		line = (yield)
		if pattern in line:
			print line

@gen.coroutine
def outer_coroutine():
	result = yield fetch_coroutine(r"http://localhost:8888/")
	print result.body , result.reason , result.code


if __name__ == '__main__':
	# IOLoop.current().run_sync(outer_coroutine)
	# IOLoop.current().spawn_callback(outer_coroutine)
	g = grep('python')
	print g.send(None)




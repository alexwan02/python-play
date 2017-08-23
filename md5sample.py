#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import hashlib

md5 = hashlib.md5()

md5.update('how to use md5 in python hashlib?')

print md5.hexdigest()


db = {
	'michael' : 'e10adc3949ba59abbe56e057f20f883e' , 
	'bob': '878ef96e86145580c38c87f0410ad153' ,
	'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user , password):
	try:
		dbpass = db[user]
		md5s = get_md5(password+ user + 'the-Salt')
		if md5s == dbpass:
			print 'True'
		else:
			print 'False'
	except KeyError:
		print 'user : %s not exist' % user

def register(username , password):
	db[username] = get_md5(password + username + 'the-Salt')

def get_md5(source):
	md5 = hashlib.md5()
	md5.update(source)
	return md5.hexdigest()

login('alex' , '123456')
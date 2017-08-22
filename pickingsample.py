try :
	import cPickle as pickle
except ImportError:
	import pickle

import json

d = dict(name = 'Bob' , age = 20 , score = 88)

print pickle.dumps(d)

with open('dump.text' , 'wb') as f:
	pickle.dump(d , f)

with open('dump.text' , 'rb') as f:
	print 'dump content = %s' % pickle.load(f)

print 'json start'
print json.dumps(d)
with open('json_dump.text' , 'wb') as f:
	json.dump(d , f)

with open('json_dump.text' , 'rb') as f:
	print 'json  = %s' % json.load(f)

class Student(object):
	def __init__(self , name , age , score):
		self.name = name
		self.age = age
		self.score = score
def student2dict(std):
	return {
		'name' : std.name , 
		'age' : std.age , 
		'score' : std.score 
	}

def dict2student(d):
	return Student(d['name'] , d['age'] , d['score'])

s = Student('Bob' , 20 , 88)
print json.dumps(s , default = student2dict)

print 'json lambda result = %s' % json.dumps(s , default = lambda obj : obj.__dict__)

with open('json_dump.text' , 'rb') as f:
	print 'json = %s' % json.loads(f.read() , object_hook = dict2student)




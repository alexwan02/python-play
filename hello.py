#!/user/bin/env python
#-*- coding : utf-8 -*-

' a test module'

__author__ = 'Alex Wan'

import sys


class Student(object):
    def __init__(self , name , score):
        self.name = name;
        self.score = score;

    def print_score(self):
        print '%s : %s ' % (self.name , self.score)


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello World!'

    elif len(args) == 2:
        print 'Hello %s !' % args[1]

    else: 
        print 'Too many arguments!'

class Chain:
    def __init__(self , path = ''):
        self._path = path

    def __getattr__(self , path):
        
        if path == 'users':
            return lambda user : Chain('%s/%s/%s' % (self._path , path , user))
        else:
            return Chain('%s/%s'  % (self._path , path))

    def __str__(self):
        return self._path

print Chain().status.users('alexwan').repo
if __name__ == '__main__':
    s1 = Student('alex' , '90')
    s2 = Student('lucky' , '100')
    s1.print_score()
    s2.print_score()
    test()

# type()
def fn(self , name='world'):
    print ('Hello %s' % name)

Hello = type('Hello' , (object , ) , dict(hello = fn)) # Create Hello Class

h = Hello()

h.hello()


# metaclass
class ListMetaclass(type):
    def __new__(cls , name , bases , attrs):
        attrs['add'] = lambda self , value : self.append(value)
        return type.__new__(cls , name , bases , attrs)

class MyList(list):
    __metaclass__ = ListMetaclass 


myList = MyList([0 , 1 , 2, 3])

myList.add(4)

print myList

# ORM
class Field(object):
    def __init__(self , name , column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__ , self.name)
    

class StringField(Field):
    def __init__(self , name):
        super(StringField , self).__init__(name , 'varchar(100)')

class IntegerField(Field):
    def __init__(self , name):
        super(IntegerField , self).__init__(name , 'bigint')

class ModelMetaclass(type):
    def __new__(cls , name , bases , attrs):
        if name == 'Model':
            return type.__new__(cls , name , bases , attrs)

        mappings = dict()
        
        for k , v in attrs.iteritems():
            if isinstance(v , Field):
                print('Found mapping : %s : %s' % (k , v))
                mappings[k] = v

        for k in mappings.iterkeys():
            attrs.pop(k)

        attrs['__table__'] = name
        attrs['__mappings__'] = mappings
        return type.__new__(cls , name  , bases , attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self , **kw):
        super(Model , self).__init__(**kw)

    def __getattr__(self , key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s' % key")
   
    def __setattr__(self , key , value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k , v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append(str(getattr(self , k , None)))
            args.append(getattr(self , k , None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__ , ','.join(fields) , ','.join(params))

        print('SQL: %s ' % sql)

        print('ARGS: %s ' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id = 12345 , name = 'alex' , email = 'alex@wan.com' , password = '***')

u.save()

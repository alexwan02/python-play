from collections import Iterable;
import os;
import functools;
age = int(raw_input('Please input yout age : '));

def showNames(names):
    print names;
print 'Your input is %d'  % age;

if age < 18:
    print 'teenager';
else:
    print 'adult';

names = ['alex' , 'bob' , 'tom'];

showNames(names);

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(10);


def hello():
    print 'exe funtion hello';

hello();

print names[0:2];

print isinstance('abc' , Iterable) , isinstance([1,2,3] , Iterable) , isinstance(123 , Iterable);


def pairs():
    for x , y in [(1 , 1) , (2 , 4) , (3 , 9 )]:
        print x , y ;

pairs();

print [d for d in os.listdir('.')];

def fib(max):
    n , a , b = 0 , 0 , 1
    while n < max:
        yield b
        a , b = b , a + b
        n = n + 1


for n in fib(45):
    print n


def str2int(s):
    def char2num(s):
        return {'0' : 0 , '1' : 1 , '2' : 2 , '3' : 3 , '4' : 4 , '5' : 5 , '6' : 6 , '7' : 7 , '8': 8 , '9' : 9 }[s]

    return reduce( lambda x , y : x * 10 + y  , map(char2num , s))

print str2int('23461');

print map(lambda s: s.title() , ['adam' , 'LISA' , 'barT'])

print reduce(lambda x , y : x * y , [1 , 2 , 3 , 4])

def log(text = 'call'):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args , **kw):
            print '%s  %s(): ' % (text , func.__name__)
            f = func(*args , **kw)
            print 'end call %s' % func.__name__
            return f
        return wrapper
    return decorator
    
@log()
def now():
    print '2014-12-25'

now()

@log('execute')
def now():
    print '2014-12-25'

now()



max2 = functools.partial(max , 10)

print max2(0 , 1 , 2, 3, 4, 5, 6, 7, 8, 9)
print max2(*range(10))
print max(range(10))

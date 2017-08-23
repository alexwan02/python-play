import sys
import os
import os.path as path


def find_all():
    args = sys.argv
     
    if len(args) <= 1 :
        print 'please input name to search'
        return 0
    else:
        count =  find_dir(args[1])
        if count == 0:
            print r"file named : '%s' not found !" % args[1]
        else:
            print 'file size : %s' % count

def find_dir(name , dir = '.'):
    count = 0 
    if dir == '.':
        dir = os.path.abspath('.')  
    
    for x in os.listdir(dir):
         
        if os.path.isdir(x):
            tmpdir = path.join(dir , x)
            count += find_dir(name , tmpdir)
        elif x.find(name) != -1:
            print path.join(dir , x)
            count += 1
    
    return count

if __name__ == '__main__':
   find_all();


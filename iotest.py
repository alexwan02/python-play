def read_file():
    try: 
        f = open('text' , 'r')
        
        print f.read()
    finally:
        if f:
            f.close()

def read_png():
    try:
        f = open('okhttp.png' , 'rb')

        print f.read()
    finally:
        if f:
            f.close

def write_file():
    with open('text' , 'w') as f :
        f.write('text write')

def os_ref():
    import os
    print os.name

def list_allfile(dir):
    

if __name__ == '__main__':
    import codecs

    print 'common read'

    read_file()

    print 'end'

    with open ('text' , 'r') as f:
        print f.read()
    
    
    with open('text' , 'r') as f:
        print 'read with line'
        for line in f.readlines():
            print(line.strip())
    
    print 'write'

   #  write_file() 
   



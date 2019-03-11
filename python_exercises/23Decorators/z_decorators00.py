from time import ctime, sleep

def tsfunc(func):
    
    def wrappedFunc():
        print ('{} function is called at {} called'.format(func.__name__,ctime()))
        return func()
    
    return wrappedFunc

# def boo():
#     print("boo called")
#      
# for i in range(3):
#     sleep(1)
#     tsfunc(boo)()
# 
# # wrappedFunc() #print line, boo() #print line 1, print line 2
 
@tsfunc
def boo():
    print("boo called")
  
for i in range(3):
    sleep(1)
    boo()

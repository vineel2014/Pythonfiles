def main():
    print("This is the functions.py file.")
    for i in myrange(50):
        print(i, end = ' ')
    
    
def myrange(*args):    
    numargs = len(args)    
    if numargs<1: raise TypeError('requires at least 1 argument')
    if numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2: 
        stop = args[1]
        start = args[0]
        step = 1
    elif numargs == 3:
        stop = args[1]
        start = args[0]
        step = args[2]
    else: raise TypeError('expected at most 3 arguments')  
    i = start
    while i <= stop:
        yield i
        i += step
if __name__ == "__main__": main()

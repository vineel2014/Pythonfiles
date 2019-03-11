def main():
    print("This is the functions.py file.")
    for i in myrange(0,25):
        print(i, end = ' ')

def myrange(start=0,stop=None,step=1):
    i = start
    while i <= stop:
        yield i
        i += step
if __name__ == "__main__": main()

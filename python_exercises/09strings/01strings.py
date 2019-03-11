def main():
    a,b = 5,42
    s = 'this is {},that is {}'
    print(s)
    print(s.format(a,b))
    print(s.format(b,a))
    s = 'this is {1},that is {0}'
    print(s.format(a,b))
    print('this is {bob},that is {fred}'.format(bob=a,fred=b))
    d=dict(bob=a,fred=b)
    print('this is {bob},that is {fred}'.format(**d))
    
    #https://docs.python.org/3/library/strings.html
    
if __name__ == "__main__": main()

def main():
    tower(3,'F','T','S')
    
def tower(n,f,t,s):
    if n ==1:
        print ('move from', f, 'to', t)
    else:
        tower(n-1,f,s,t)
        tower(1,f,t,s)
        tower(n-1,s,t,f)


if __name__ == "__main__": main()

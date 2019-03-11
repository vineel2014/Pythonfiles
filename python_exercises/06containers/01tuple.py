def main():
    t = 1
    print(type(t))
    
    t = (1,)
    print(type(t))
    
    t = 1,
    print(type(t))
    
    t = (1,2,3,4,8)
    print(t)
    print(t[0],t[-1])
    print(len(t))
    print(min(t))
    print(max(t))


if __name__ == "__main__": main()

def main():
    import random
    
    print(random.randint(1,1000))
    print(random.choice((1,2,3,4,5,'a','b','c','d')))
    print(random.choice((1,2,3,4,5,'a','b','c','d')))
    print(random.random())
    
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
   
    
if __name__ == "__main__": main()

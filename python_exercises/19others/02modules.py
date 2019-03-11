def main():
    import random
    
    print(random.randint(1,1000))
    
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    
if __name__ == "__main__": main()

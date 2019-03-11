def main(): #Splitting & Joining
    s = 'Rats are small, Cats are big'
    print(s.split())
    print(s.split('are'))
    
    words = s.split('are')
    print(' are '.join(words))
    
if __name__ == "__main__": main()

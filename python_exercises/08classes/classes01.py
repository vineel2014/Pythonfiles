#with constructor
class Duck:
    
    def __init__(self,x): #used for initializing data
        self.x = x
        print(self)
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck(5) # donald is the instance of class Duck
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()

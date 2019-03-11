#Encapsulation
class Duck:
    
    def __init__(self,value):
        self._v = value
        
    def quack(self):
        print('Quaaack!', self._v)

    def walk(self):
        print('Walks like a duck.', self._v)

def main():
    donald = Duck(100) 
    donald.quack()
    donald.walk()
    
    frank = Duck(200) # Encapsulation - Value is in object & not in class
    frank.quack()
    frank.walk()

if __name__ == "__main__": main()

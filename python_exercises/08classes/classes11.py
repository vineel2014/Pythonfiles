class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

class Dog:
    def bark(self):
        print('Bark!')
    def fur(self):
        print('the dog has brown & white far')
        
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    
    fido = Dog()
    fido.bark()
    fido.fur()
    
if __name__ == "__main__": main()

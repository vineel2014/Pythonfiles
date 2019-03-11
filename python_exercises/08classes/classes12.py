class Duck:
    def bark(self):
        print("Duck can't bark!")
    def fur(self):
        print('the duck has feathers')
    def quack(self):
        print('Quaaack!')
    def walk(self):
        print('Walks like a duck.')

class Dog:
    def bark(self):
        print('Bark!')
    def fur(self):
        print('the dog has brown & white fur')
    def quack(self):
        print("Dog can't quack")
    def walk(self):
        print('Walks like a dog.')
        
def main():
    donald = Duck()
    fido = Dog()
    
    for o in (donald,fido):
        o.bark()
        o.fur()
        o.quack()
        o.walk()
        print ('\n')
if __name__ == "__main__": main()

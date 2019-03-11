#Polymorphism: refers to a programming language's ability to process objects differently depending on their data type or class.
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
        
def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    in_the_pond(fido)


if __name__ == "__main__": main()

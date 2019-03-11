#super() function

class Animal:
    def talk(self):
        print('I am a talking animal')
    def walk(self):
        print('I am a walking animal')

class Duck(Animal):
    def quack(self):
        print('Quaaack!')
    def walk(self):
        super().walk()
        print('Walks like a duck.')

def main():
    donald = Duck() 
    donald.quack()
    donald.walk()
    donald.talk()

if __name__ == "__main__": main()

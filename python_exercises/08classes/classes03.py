#Default Value & Change Value
class Duck:
    
    def __init__(self, color = 'white'): #used for initializing data
        self._color = color #underscore to specify that this will not be changed from outside of the method
    
    def get_color(self):
        return self._color

def main():
    donald = Duck() 
    print (donald.get_color())
    donald._color = 'blue'
    print (donald.get_color())

if __name__ == "__main__": main()


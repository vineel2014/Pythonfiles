#Method to reset value

class Duck:
    
    def __init__(self, color = 'white'): 
        self._color = color
        self._feetcolor = color
          
    def set_color(self,color):
        self._color = color
        self._feetcolor = color

    def get_color(self):
        return (self._color, self._feetcolor)
    

def main():
    donald = Duck() 
    print (donald.get_color())
    donald.set_color('blue')
    print (donald.get_color())
    
if __name__ == "__main__": main()

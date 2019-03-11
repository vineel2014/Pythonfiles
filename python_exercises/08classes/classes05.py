#dictionary argument for multiple variables
class Duck:
    
    def __init__(self, **kwargs): 
        self._color = kwargs.get('color','not defined') 
        self._eyes = kwargs.get('eyes','not defined')
        
    def set_color(self,color):
        self._color = color

    def get_color(self):
        return self._color
    
    def set_eyes(self,eyes):
        self._eyes = eyes

    def get_eyes(self):
        return self._eyes

def main():
    donald = Duck(color='blue',eyes=2) 
    print (donald.get_color())
    print (donald.get_eyes())
    
    frank = Duck()  
    print (frank.get_color())
    print (frank.get_eyes())
    
if __name__ == "__main__": main()

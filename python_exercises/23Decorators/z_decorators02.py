class Duck:
    
    def __init__(self, **kwargs): 
        self.variables = kwargs
  
    def set_variable(self,k,v):
        self.variables[k] = v

    def get_variable(self,k):
        return self.variables.get(k,None)
    
    #accessor methods
    @property
    def color(self): #color = property(color)
        return self.variables.get('color',None)
    
    @color.setter 
    def color(self,c):
        self.variables['color'] = c    
    
    @color.deleter
    def color(self,c):
        del self.variables['color']
     
        
def main():
    donald = Duck()
    donald.color = 'green'
    print(donald.color)
    
    
#     frank = Duck(color='blue',size = 'small', feet = 2, eyes = 2)
#     frank.set_variable('ears', 2)
#     frank.set_variable('eyes', 1)
#        
#     print (frank.get_variable('color'))
#     print (frank.get_variable('size'))
#     print (frank.get_variable('feet'))
#     print (frank.get_variable('eyes'))
#     print (frank.get_variable('ears'))
#     print (frank.get_variable('tail'))
   
if __name__ == "__main__": main()

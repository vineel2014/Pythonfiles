class Duck:
    
    def __init__(self, **kwargs): 
        self.variables = kwargs
  
    def set_variable(self,k,v):
        self.variables[k] = v

    def get_variable(self,k):
        return self.variables.get(k,None)
    
    @property
    def color(self): #color = property(color)
        return self.variables.get('color',None)
    
    @color.setter #color = property.setter(color)
    def color(self,c):
        self.variables['color'] = c
    
    
    @color.deleter #color = property.deleter(color)
    def color(self,c):
        del self.variables['color']
     
        
def main():
    donald = Duck()
    donald.color = 'green'
    donald.color = 'blue'
    print(donald.get_variable('color'))
    
   
if __name__ == "__main__": main()

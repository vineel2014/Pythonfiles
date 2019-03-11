class Duck:
    
    def __init__(self, **kwargs): 
        self.variables = kwargs
  
    def set_variable(self,k,v):
        self.variables[k] = v

    def get_variable(self,k):
        return self.variables.get(k,None)
     
        
def main():
    donald = Duck()
    donald.set_variable("color","blue")
    print(donald.get_variable('color'))
   

if __name__ == "__main__": main()

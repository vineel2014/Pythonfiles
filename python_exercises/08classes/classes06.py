# Making it dynamic
class Duck:
    
    def __init__(self, **kwargs): 
        self.variables = kwargs
  
    def set_variable(self,k,v):
        self.variables[k] = v

    def get_variable(self,k):
        return self.variables.get(k,None)
    

def main():
   
    frank = Duck(color='blue',size = 'small', feet = 2, eyes = 2,feathers = 'white')
    frank.set_variable('ears', 2)
    frank.set_variable('eyes', 1)
       
    print (frank.get_variable('color'))
    print (frank.get_variable('size'))
    print (frank.get_variable('feet'))
    print (frank.get_variable('eyes'))
    print (frank.get_variable('ears'))
    print (frank.get_variable('tail'))
    print (frank.get_variable('feathers'))
    
if __name__ == "__main__": main()

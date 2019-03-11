#def main():

#    print("This is the syntax.py file.")

#    egg()





def egg():

    print("egg is called")

def hello():
    
    print("Hello anil")

def Pass():
    a=int(input("enter number")) 
     
    while (a<5):
           
      print("equal")
      a+=2  
    else:
      
      print("else is processsed") 

def evenodd():
    j=int(input("Enter max range"))
    for i in range(2,j,2):
       print (i)
       

def main():

    print("This is the syntax.py file.")
    egg()
    hello()
    Pass()
    evenodd()


if __name__ == "__main__": main()




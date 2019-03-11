def main():
    
    print (5<6)
    print (5>6)
    print (5==6)
    print (5<=6)
    print (5>=6)
    print (5!= 6)
    
    x,y= 100.001,100.001
    print ('line 11', x is y)
    
    x,y = 2.25,1.25+1.0
    print (x == y)
    print (x is y)    
    
    x,y= (1,2),(1,2)
    print (x is not y)
    
if __name__ == "__main__": main()

def main():
    x = 42
    print (x,'\t',id(x),'\t',type(x))
    
    x = "Hello"#Variables in Python are references to objects
    print (x,'\t',id(x),'\t',type(x))
    
if __name__ == "__main__": main()

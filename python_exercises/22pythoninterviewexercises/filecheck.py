try:
    with open("welcome","r") as f:

        print(f.read())
        
    f.close()        

    with open("welcome","r") as f:

       for i in len(f.readline()):

           print(len(f.readline().rstrip()))

        #print(f.read())
    f.close()

except IOError:
    print("No such file exits")

from datetime import datetime
def ObtainDate():
    isValid=False
    while not isValid:
        userIn = str(input("Type Date dd/mm/yy: "))
        #"print(userIn)
        #print (userIn.strptime('We are the %d, %b %Y'))
        try:
            d = str(datetime.strptime(userIn, "%d/%m/%y"))[:10]
            isValid=True
        except:
            print ("Doh, try again!\n")
            
    return d
print (ObtainDate())
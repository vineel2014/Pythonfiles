def main():
    LeapYear(2000)
    
#Leap Years are any year that can be evenly divided by 4 (such as 2012, 2016, etc)
#         except if it can can be evenly divided by 100, then it isn't (such as 2100, 2200, etc)
#              except if it can be evenly divided by 400, then it is (such as 2000, 2400)

def LeapYear(x):
    x = int(x)
    y = []
    for i in (4,100,400):
        if not divmod(x,i)[1]:
            y.append(i)
           
    if y == [4] or y == [4,100,400]:
        print(x,'is a leap year')
    else:
        print(x,'is not a leap year')
       
      
if __name__ == "__main__": main()
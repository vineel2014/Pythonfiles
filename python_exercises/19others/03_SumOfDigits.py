def main():
    
    x = int(input("enter an integer"))
    sumDigits = 0
    for c in str(x):
        sumDigits += int(c)
    print (sumDigits)

if __name__ == "__main__": main()
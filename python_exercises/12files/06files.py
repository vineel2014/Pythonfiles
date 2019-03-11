def main(): #Binary Files
    f = open('olives.jpg','rb')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()

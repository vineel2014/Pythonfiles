def main():
    f = open('lines.txt','r')
    for line in f:
        print(line, end = '')

if __name__ == "__main__": main()


# f = open('lines.txt','w')
# f = open('lines.txt','a')
# f = open('lines.txt','r+')
# f = open('lines.txt','rb')
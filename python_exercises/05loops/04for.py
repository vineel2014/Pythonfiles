def main():
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index,line, end = '')
    fh.close()
if __name__ == "__main__": main()

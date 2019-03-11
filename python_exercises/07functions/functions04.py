def main():
    testfunc()
    testfunc(52,53,54)
    testfunc(52,anothermore=54)

def testfunc(number=42,another=43,onemore=44,anothermore=67):
    print('This is a test function',number,another,onemore,anothermore)

if __name__ == "__main__": main()

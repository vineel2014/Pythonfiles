def main():
    testfunc(one = 1, two = 2, four = 42)

def testfunc(**kwargs):
    print(kwargs)
    print(kwargs['one'],kwargs['two'],kwargs['four'])

if __name__ == "__main__": main()

def main():
    print(isPal('abcbba'))
    
def isPal(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and isPal(s[1:-1])


if __name__ == "__main__": main()

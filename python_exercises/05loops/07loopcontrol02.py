def main():
    s = 'this is a string'
    print(len(s))
    i = 0
    while (i<len(s)):
        if s[i] == 's': break
        i += 1
        if s[i-1] == 's': continue
        print(s[i-1], end='')
        
    else:#if loop is false
        print('else is printed')
        
if __name__ == "__main__": main()

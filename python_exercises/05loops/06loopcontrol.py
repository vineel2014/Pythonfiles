def main():
    s = 'this is a string'
    for c in s:
        if c=='s': continue
        #if c == 's': break
        print(c, end='')
    else:#if loop is false
        print('\n else is printed')
        
if __name__ == "__main__": main()

def main():
    foostr = ['a','b','c','d','e']
    x = len(foostr)
    r = []
    for i in range(0,x,2):
        try:
            r += foostr[i+1]+foostr[i]
        except IndexError:
            r += foostr[i]
    print(r)

if __name__ == "__main__": main()
def main():
    d = {'one':1,'two':2,'three':3}
    print(d)
    x = dict(four=4,five=5,six=6)
    print(x)
    c = dict(seven=7,eight=8,**x)
    print(d.values())
    print(c)
    print('one' in d, 'four' in d)
    for k in c: print(k, end=' ')
    print()
    for k,v in d.items(): print(k,v)
    print(d['one'])
    for k in d.keys(): print(k)
    #print(d['four'])
    print(d.get('one'),d.get('four'),d.get('four','Not Found'))
    del d['one']
    print(d)
    print(d.pop('two'), d)
    

if __name__ == "__main__": main()

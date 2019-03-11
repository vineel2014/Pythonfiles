def mytri(myrange):
    rows = list()
    lr = None # Last row

    for i in xrange(myrange+1):
        try:
            #print [1]
            #print lr[i]
            #print lr[t+1]
            lr = [1] + [lr[i] + lr[i+1] for i in range(len(lr) - 1)] + [1]
        except TypeError:
            lr = [1]
        #rows.append(str(lr))
        rows.append(' '.join(str(v) for v in lr))
    return rows

rows = mytri(10)
l = len(rows[-1])
print '\n'.join(v.center(l) for v in rows)

    

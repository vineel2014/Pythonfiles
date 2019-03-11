

book=open('treasure.txt','r')


n_chars=0

for line in book:
    n_chars+=len(line)

print(n_chars)

book.close()








book=open('treasure.txt','r')

n_lines=0

for line in book:
    n_lines+=1

print(n_lines)

book.close()




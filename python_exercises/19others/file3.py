

book=open('treasure.txt','r')

n_lines=0
n_words=0
n_chars=0

for line in book:
    n_lines+=1
    n_words+=len(line.split())
    n_chars+=len(line)

print("number of lines in the given file:",n_lines)
print("number of words in the given file:",n_words)
print("number of characters in the given file:",n_chars)

book.close()






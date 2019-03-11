def translate(s):
    print("output in Sweedish Robber's Language for:",s)
    consonants = 'bcdfghjklmnpqrstvwxz'
    return ''.join(l + 'o' + l if l in consonants else l for l in s)
#print("output in Sweedish Robber's Language")
st=input("enter a string")
print(translate(st))
def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return not (set(alphabet) - set(phrase))
st=input("enter a string")
b=is_pangram(st)
print("pangram:",b)
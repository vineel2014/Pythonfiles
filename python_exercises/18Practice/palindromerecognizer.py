import string
ignored = string.punctuation + " "
def is_palindrome(str1):
    cleanstr = ""
    for i in str1:
        cleanstr += "" if i in ignored else i # I love Python ternary operator

    return cleanstr.lower() == cleanstr[::-1].lower()

#test
print (is_palindrome("Go hang a salami I'm a lasagna hog."))
print (is_palindrome("Was it a rat I saw?"))
print (is_palindrome("Step on no pets"))
print (is_palindrome("Sit on a potato pan, Otis!"))
print (is_palindrome("Lisa Bonet ate no basil"))
print (is_palindrome("Satan, oscillate my metallic sonatas"))
print (is_palindrome("I roamed under it as a tired nude Maori"))
print (is_palindrome("Rise to vote sir"))
print (is_palindrome("Dammit, I'm mad!"))
print (is_palindrome("This is not a palindrome"))
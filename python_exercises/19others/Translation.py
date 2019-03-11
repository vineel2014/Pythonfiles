EtoF = {'bread':'du-pain', 'wine':'du-vin',\
    'eats':'mange', 'drinks':'bois',\
        'likes':'aime',1:'un','6.00':'6.00'}

def translateWord(word,EtoF):
    if word in EtoF:
        return EtoF[word]
    else:
        return word
    
def translate(sentence):
    word = ''
    translation = ''
    for i in sentence:
        if i != ' ':
            word += i
        else:
            translation += translateWord(word, EtoF) + ' '
            word = ''
    return translation + translateWord(word, EtoF)

def main():
    print (translate('John eats bread & drinks wine'))
    
if __name__ == "__main__": main()

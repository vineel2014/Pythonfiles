def main():
    print(translate('Vinayak drinks wine and eats bread. He is number one tester'))
    
E2F = {'bread':'du pain', 'wine':'du vin',\
       'eats':'mange','drinks':'bois',\
       'likes':'aime', 'one':'un',\
       '6.00':'6.00'}

def translateWord(word,dictionary):
    if word in dictionary:
        return dictionary[word]
    else:
        return word

def translate(sentence):
    sentence = sentence + ' '
    translation = ''
    word = ''
    for c in sentence:
        if c!= ' ':
            word += c
        else:
            translation = translation + ' ' +\
                          translateWord(word,E2F)
            word = ''
    return translation[1:]

if __name__ == "__main__": main()
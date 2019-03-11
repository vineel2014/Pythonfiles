def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth'            
    )
    
    #print(choices['seven'])
    print(choices.get('two','other'))

if __name__ == "__main__": main()

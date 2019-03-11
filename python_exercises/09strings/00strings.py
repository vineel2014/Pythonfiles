def main():
    print('this is a string'.upper())
    print('this is a string {}'.format(42))
    s = 'this is a string'
    print(s.capitalize())
    print(s.title())
    print(s.upper())
    print(s.upper().lower())
    print(s.swapcase())
    print(s.find('is'))
    print(s.replace('this', 'that'))
    print(s.strip())
    print(s.rstrip('ing'))
    print(s.isalnum())
    print(s.isalpha())
    print(s.isdigit())
    print(s.isprintable())
    
if __name__ == "__main__": main()

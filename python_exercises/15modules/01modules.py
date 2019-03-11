def main():
    
    import urllib.request
    page = urllib.request.urlopen("https://www.google.co.in/?gws_rd=ssl")
    
    for line in page: print (str(line, encoding = 'utf_8'), end='')
    
if __name__ == "__main__": main()


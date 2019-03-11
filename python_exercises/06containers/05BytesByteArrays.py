def main():# byte arrays holds 8 bit data
    #utf_8 is not handled properly
    fin = open('utf8.txt','r',encoding='utf_8')
    fout = open('utf8.html', 'w')
    
    outbytes = bytearray()
    
    for line in fin:
        for c in line:
            if ord(c)<=127: #till 127 unicode is same as ascii ord(b'a') = ord('a')
                outbytes.append(ord(c))
            else: # from 127 till 256 ascii is different
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding='utf_8') #&# is for html
    
    #print(outbytes)           
    
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr,file = fout)
    
    print ('Done!')
    
if __name__ == "__main__": main()

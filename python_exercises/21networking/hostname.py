import sys, socket

result = socket.getaddrinfo('www.google.com', None, 0, socket.SOCK_STREAM)

counter = 0

for item in result:

    print ("%-2d: %s" % (counter, item[4]))
    
    counter += 1




import sys, socket

# get match all corrosponding hosts

result = socket.getaddrinfo("www.google.com", None)

counter = 0

for item in result:

    print ("%-2d: %s" % (counter, item[4]))

    counter += 1



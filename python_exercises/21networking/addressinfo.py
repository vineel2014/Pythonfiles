import sys, socket

result = socket.getaddrinfo("192.1.1.100", None)

print(result[0][4])

print(result)

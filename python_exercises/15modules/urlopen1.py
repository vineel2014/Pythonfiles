import urllib.request, urllib.error, urllib.parse
response = urllib.request.urlopen('http://python.org/')
html = response.read()

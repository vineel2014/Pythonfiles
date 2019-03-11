import whois  # i'm using this http://cryto.net/pythonwhois

domain=input("ENTER DOMAIN NAME(ex: www.google.com):")

details = whois.whois(domain)

print (details)



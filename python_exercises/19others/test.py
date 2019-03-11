listofitems = [1,2,3,4,0.5,0.6]
listofitems2 = ['a','b','c','d','e','f']
listofitems3 = ['a1','s1','d3','4f','f4']
debug = True 
for command in ("Rscript script.R --args %s %s %s" % (one, two, three)
                             for one in listofitems
                             for two in listofitems2
                             for three in listofitems3):
  if debug:
     print(command)
  else:
     subprocess.call(command , shell=True)

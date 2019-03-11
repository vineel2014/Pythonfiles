import xml.etree.ElementTree as xml

#Construct xml
rootx = xml.Element('Books')
childx = xml.SubElement(rootx,'TheLittlePrince')
childx.text = 'Old Book'
childx.attrib = dict(author = "expry", subject = "philosophy")
xmlstring = xml.tostring(rootx)
print (xmlstring)

#Write File
xmlFile = open('xml2.xml','wb')
xmlFile.write(xmlstring)
xmlFile.close()

#Read File
tree = xml.parse('xml2.xml')
rooty = tree.getroot()

print(rooty.tag,rooty.attrib,rooty.text)
for i in rooty:
    print(i.tag,i.attrib,i.text)

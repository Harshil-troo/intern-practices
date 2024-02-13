import xml.etree.ElementTree as ET

# tree = ET.parse("myxml.xml")
# print(tree.getroot)
# for x in tree.getroot()[0]:
#     print(x.tag,x.attrib,x.text)

# for x in tree.findall("employee"):
#     print(x.find('name').text)
#     print(x.find('age').text)
#     print(x.find('address').text)

# for x in tree.iter("address"):
#     print(x.text)
#     a = str(x.text)+ " Smart City"
#     x.text = str(a)
#     x.set("updated","City")
#
# tree.write("myxml2.xml")

# for x in tree.findall("employee"):
#     skills = ET.SubElement(x,"skills")
#     skills.text = "Python Lover"
# tree.write("myxml3.xml")
#
# print(tree.getroot()[0][2].attrib.pop("updated"))
# tree.write("myxml2.xml")

# print(tree.getroot()[0][0])
# tree.getroot()[0].remove(tree.getroot()[0][0])
# tree.write("myxml2.xml")
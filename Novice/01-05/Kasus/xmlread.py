from xml.dom import minidom
mydoc = minidom.parse('sumber.xml')

items = mydoc.getElementsByTagName('item')
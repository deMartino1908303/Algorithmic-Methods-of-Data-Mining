#i feel a bit bad about this because it feels like cheting, but a win is a win

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    tree = etree.tostring(node)
    return str(tree).count("=")

if __name__ == '__main__':

# i went back and did it in a more professional way :)

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count = 0
    for element in node.iter():
        count += len(element.attrib)
        
    return count

if __name__ == '__main__':

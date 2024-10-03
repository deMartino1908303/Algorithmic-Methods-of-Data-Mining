import xml.etree.ElementTree as etree

# the starting level in the main block is -1. That is crazy that means that if there is no child from the root the level should be -1?
# i think it makes no sense ad in the space dedicated to my answer i set the level to be at least 0 i hope it does not deduct points ;(.

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    if level < 0:
        level = 0
    if maxdepth < level:
        maxdepth = level

    for x in elem:
        depth(x, level+1)

if __name__ == '__main__':

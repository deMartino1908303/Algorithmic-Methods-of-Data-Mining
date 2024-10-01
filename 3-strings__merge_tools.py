from collections import OrderedDict
from itertools import islice

def merge_the_tools(string, k):
    # your code goes here

    sbstr_num = int(len(string)/k)
    y = []
    sbstr_len = k
    start = 0
    for _ in range(sbstr_num):
        y.append(list(islice(string, start,sbstr_len)))
        start += k
        sbstr_len += k
    for x in y:
        print("".join(list(OrderedDict.fromkeys(x))))

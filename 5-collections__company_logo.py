#!/bin/python3

from collections import Counter


if __name__ == '__main__':
    s = input()
    count = list(Counter(s).most_common())
    count = sorted(count, key=lambda x: (-x[1], x[0]))
    
    for pair in count[0:3]:
        print(pair[0], pair[1])

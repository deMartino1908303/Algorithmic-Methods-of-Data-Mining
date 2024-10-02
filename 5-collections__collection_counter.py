# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

trash, shoes, iterable = input(), input().split(), int(input())

shoes = dict(Counter(shoes))
earnings = 0
while iterable > 0:
    
    tmp = input().split()
    size = tmp[0]
    
    if size in shoes.keys():
        if shoes[size] > 0:
            shoes[size] = shoes[size] -1
            earnings += int(tmp[1])
            
    iterable -= 1
print(earnings)

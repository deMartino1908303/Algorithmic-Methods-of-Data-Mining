# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
iteration = int(input())
dic = OrderedDict()
while iteration > 0:
    word = input()
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1
    iteration -= 1
    
print(len(dic))

res = " ".join(list(map(str, list(dic.values()))))
print(res)

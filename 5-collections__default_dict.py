# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
leng= input().split()

grpA= defaultdict(list)

for x in range(1,int(leng[0])+1):
    tmp = input()
    grpA[tmp].append(str(x))

for y in range(int(leng[1])):
    tmp1 = input()
    ver = tmp1 in dict(grpA).keys()
    if ver:
        print(" ".join(grpA.get(tmp1)))
    else:
        print("-1")

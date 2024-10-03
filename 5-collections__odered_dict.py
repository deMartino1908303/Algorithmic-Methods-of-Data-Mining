# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n_itm = int(input())
item_dic = OrderedDict()
while n_itm > 0 :
    itm = input().split()
    itm_cost = int(itm.pop(-1))
    itm_name = " ".join(itm)
    if itm_name in item_dic.keys():
        item_dic[itm_name] = item_dic.get(itm_name) + itm_cost
    else:
        item_dic.setdefault(" ".join(itm), itm_cost)
    n_itm -=1

for x in item_dic.keys():
    print(x, item_dic[x])

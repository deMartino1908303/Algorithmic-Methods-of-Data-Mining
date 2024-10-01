# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
useless = input()
obj_list = Counter(input().split())
like = list(input().split())
dislike = list(input().split())
happy = 0
for x in like : happy += obj_list[x]
for y in dislike : happy -= obj_list[y]

print(happy)

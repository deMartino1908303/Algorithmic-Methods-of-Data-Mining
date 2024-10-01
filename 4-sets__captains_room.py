# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
useless = input()
rooms = Counter(input().split())
sorted(rooms.elements())
print(list(rooms)[-1])

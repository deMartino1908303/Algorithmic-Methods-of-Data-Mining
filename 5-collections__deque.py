# Enter your code here. Read input from STDIN. Print output to STDOUT
# it feels bad as there must be other ways to do this that with if-else

from collections import deque
d = deque()

iterable = int(input())

while iterable > 0:
    to_do = input()
    if "left" in to_do :
        if "pop" in to_do :
            d.popleft()
        else:
            d.appendleft(int(to_do[-1]))
    elif 'pop' in to_do:
        d.pop()
    else:
        d.append(int(to_do[-1]))
    iterable -=1
print(*d)

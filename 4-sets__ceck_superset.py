# Enter your code here. Read input from STDIN. Print output to STDOUT

super_set = set(map(int, input().split()))

iterable = int(input())
supa_cool = True

while iterable > 0:
    qui = set(map(int, input().split()))
    if len(qui) >= len(super_set):
        supa_cool = False
        break
    elif len(qui.difference(super_set)) != 0:
        supa_cool = False
        break
    iterable -= 1
print(supa_cool)

n = int(input())
s = set(map(int, input().split()))
iter_num = int(input())
for _ in range(0, iter_num):
    comand = input()
    if " " in comand:
        if "m" in comand:
            s.remove(int(comand[-1]))
        else:
            s.discard(int(comand[-1]))
    else:
        s.pop()
        
print(sum(s))

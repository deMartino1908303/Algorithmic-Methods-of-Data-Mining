# Enter your code here. Read input from STDIN. Print output to STDOUT

iterable = int(input())

while  iterable > 0:
    trash_1, set_1, trash_2, set_2 = input(), input().split(), input(), input().split()
    set_1 = set(map(int, set_1))
    set_2 = set(map(int, set_2))
    if len(set_1.difference(set_2)) != 0: 
        print(False)
    else:
        print(True)
    iterable -= 1

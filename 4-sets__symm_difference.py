# Enter your code here. Read input from STDIN. Print output to STDOUT

trash, set_1, trashh, set_2 = input(), input(), input(), input()

set_1 = set(map(int, set_1.split(" ")))
set_2 = set(map(int, set_2.split(" ")))

common = sorted(set(set_1).symmetric_difference(set(set_2)))

for i in common:
    print(i)

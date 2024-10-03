# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

iterable = int(input())
division = iterable
names = input().split()
tup_obj = namedtuple("tup_obj", names)
grades = 0
while iterable > 0:
    temp_line = input().split()
    xyz = tup_obj(temp_line[0], temp_line[1], temp_line[2], temp_line[3])
    grades += int(xyz.MARKS)
    iterable -=1
    
print(round(grades/division, 2))

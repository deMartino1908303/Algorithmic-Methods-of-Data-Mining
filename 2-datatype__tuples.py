# usualy i use python3 nut the has valuew in python 3 differ from pypy 3 an di had to use pypy 3

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = tuple(integer_list)
    print(hash(tup))

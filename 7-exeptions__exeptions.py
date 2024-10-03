# Enter your code here. Read input from STDIN. Print output to STDOUT

iterable = int(input())

while iterable > 0:
    
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ValueError as e:
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    iterable -=1

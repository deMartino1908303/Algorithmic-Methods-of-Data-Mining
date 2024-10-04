# Enter your code here. Read input from STDIN. Print output to STDOUT

x, result= list(map(int, input().split()))

operation = input()

print(eval(operation)==result)

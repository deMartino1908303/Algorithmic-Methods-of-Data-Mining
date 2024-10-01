# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
big_list = [input() for _ in range(0, num)]

print(len(set(big_list)))

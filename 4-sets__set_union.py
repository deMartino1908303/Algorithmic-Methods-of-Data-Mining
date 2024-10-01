# Enter your code here. Read input from STDIN. Print output to STDOUT
en = int(input())
en_np = set(input().split())
fr = int(input())
fr_np = set(input().split())

print ( len((en_np|fr_np)))

# Enter your code here. Read input from STDIN. Print output to STDOUT

info = input().split()
count = 1
while count < int(info[0]):
    print((".|." * count).center(int(info[1]), "-"))
    count += 2
    
print("WELCOME".center(int(info[1]), "-"))
count -= 2

while count > 0:
    print((".|." * count).center(int(info[1]), "-"))
    count -= 2
    

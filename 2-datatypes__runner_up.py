if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

l=[x for x in arr]
l.sort()
#print(n,l)
tmp=l[n-1]

while tmp==l[n-1]:
    del l[n-1]
    n-=1
    #print(n, l)

print (l[n-1])

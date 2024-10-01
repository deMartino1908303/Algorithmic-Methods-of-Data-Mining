if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

l = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
lf=[]

for tem in l :
    if tem[0]+tem[1]+tem[2] != n :
        lf.append (tem)
    
print (lf)

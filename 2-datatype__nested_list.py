if __name__ == '__main__':
    l = []
    sl = []
    fnl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        tmp = [score, name]
        sl.append(score)
        l.append(tmp)
    
    l.sort(reverse=True)
    last = len(l)-1
    cntr=l[last][0]
    while cntr == l[last][0] :
        l.pop(len(l)-1)
        last = len(l)-1

    last = len(l)-1
    
    if sl.count(l[last][0])== 1 :
        print (l[last][1])
    else:
        
        for grp in l:
            if grp[0]==l[last][0]:
                tmp= grp[1]
                fnl.append(tmp)
        
        fnl.sort()
        
        for nm in fnl:
            print (nm, end='\n')

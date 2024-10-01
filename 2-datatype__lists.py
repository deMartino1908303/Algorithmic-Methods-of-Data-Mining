if __name__ == '__main__':
    N = int(input())
    l=[]
    
    for trash in range(N) :
        
        CMD = list(input().split())

        if CMD[0] == "insert" :
            l.insert(int(CMD[1]), int(CMD[2]))
            
        elif CMD[0] == "print" :
            print (l)
        
        elif CMD[0] == "remove" :
            l.remove(int(CMD[1]))
        
        elif CMD[0] == "append" :
            l.append(int(CMD[1]))
        
        elif CMD[0] == "sort" :
            l.sort()
        
        elif CMD[0] == "pop" :
            l.pop()
        
        elif CMD[0] == "reverse" :
            l.reverse()
        

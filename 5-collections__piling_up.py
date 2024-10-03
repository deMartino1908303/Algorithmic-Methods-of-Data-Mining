# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n_itr = int(input())
while n_itr > 0 :
    steps = int(input())
    block = deque(input().split())
    val = 2147483648
    while steps > 0 :
        test1 = int(block[0]) <= int(val)
        test2 = int(block[-1]) <= int(val)
        if test1 and test2:
            
            if int(block[0])>int(block[-1]):
                val = block.popleft()
            else:
                val = block.pop()
                
        elif test1 :
            val = block.popleft()
                
        elif test2 :
            
            val = block.pop()
        else:
            
            print('No')
            break
        
        steps-=1
    
    if steps == 0:
        print('Yes')
    n_itr-=1

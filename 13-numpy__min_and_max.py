import numpy



iteration, trash = list(map(int, input().split()))
arr = []

while iteration>0:
    tmp = [int(x) for x in input().split()]
    arr.append(tmp)
    iteration -= 1
    
print(numpy.max(numpy.min(numpy.array(arr), axis=1)))

import numpy

iteration, trash = list(map(int, input().split()))
arr = []
while iteration > 0:
    tmp_arr = [int(x) for x in input().split()]
    
    arr.append(tmp_arr)
    
    iteration -=1

print(numpy.prod(numpy.sum(numpy.array(arr), axis=0)))

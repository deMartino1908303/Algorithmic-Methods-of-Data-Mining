import numpy


iteration = int(input())
arr = []
while iteration > 0:
    tmp_arr = [float(x) for x in input().split()]
    
    arr.append(tmp_arr)
    
    iteration -=1
    
print(round(numpy.linalg.det(numpy.array(arr)), 2))

import numpy




iteration, trash = list(map(int, input().split()))
arr = []
while iteration > 0:
    tmp_arr = [int(x) for x in input().split()]
    
    arr.append(tmp_arr)
    
    iteration -=1
    
arr = numpy.array(arr)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr), 11))

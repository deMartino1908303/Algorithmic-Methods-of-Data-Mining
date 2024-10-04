import numpy

iterator = list(map(int, input().split()))
arr = []
while iterator[0] > 0:
    values = list(map(int, input().split()))
    arr.append(values)
    iterator[0] -= 1

arr = numpy.array(arr)
print(numpy.transpose(arr))

print(arr.flatten())

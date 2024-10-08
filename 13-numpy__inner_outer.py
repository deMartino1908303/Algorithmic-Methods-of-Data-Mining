import numpy



arr_1 = numpy.array([int(x) for x in input().split()])

arr_2 = numpy.array([int(x) for x in input().split()])

print(numpy.inner(arr_1, arr_2))
print(numpy.outer(arr_1, arr_2))

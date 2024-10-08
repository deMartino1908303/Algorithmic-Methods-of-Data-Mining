import numpy



arr = numpy.array([float(x) for x in input().split()])

x = int(input())

print(numpy.polyval(arr, x))

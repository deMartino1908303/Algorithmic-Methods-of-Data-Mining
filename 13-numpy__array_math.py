import numpy


iteration, trash = list(map(int, input().split()))

arr_1 = numpy.array([list(map(int, input().split())) for _ in range(iteration)])

arr_2 = numpy.array([list(map(int, input().split())) for _ in range(iteration)])


print(numpy.add(arr_1, arr_2))
print(numpy.subtract(arr_1, arr_2))
print(numpy.multiply(arr_1, arr_2))
print(numpy.floor_divide(arr_1, arr_2))
print(numpy.mod(arr_1, arr_2))
print(numpy.power(arr_1, arr_2))

import numpy



iteration = int(input())

arr_1 = numpy.array([list(map(int, input().split())) for _ in range(iteration)])
arr_2 = numpy.array([list(map(int, input().split())) for _ in range(iteration)])

print(arr_1 @ arr_2)

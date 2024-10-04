import numpy

iterator1, iterator2, bazinga = list(map(int, input().split()))
ls_1 = []
ls_2 = []
while iterator1 > 0:
    inp = list(map(int, input().split()))
    ls_1.append(inp)
    iterator1 -= 1
    
while iterator2 > 0:
    inp = list(map(int, input().split()))
    ls_2.append(inp)
    iterator2 -= 1
    
ls_1 = numpy.array(ls_1)
ls_2 = numpy.array(ls_2)


print(numpy.concatenate([ls_1, ls_2]))

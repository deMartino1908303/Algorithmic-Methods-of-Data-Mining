# Complete the solve function below.
def solve(s):
    l_f=[]
    l=s.split(" ")
    for var in range(len(l)):
        tmp = l[var].capitalize()
        l_f.append(tmp)
    fin = ' '.join(l_f)
    return fin

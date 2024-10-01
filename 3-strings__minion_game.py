# Complete the solve function below.
def solve(s):
    lf=[]
    l=s.split(" ")
    for var in range(len(l)):
        tmp = l[var].capitalize()
        lf.append(tmp)
    fin = ' '.join(lf)
    return fin

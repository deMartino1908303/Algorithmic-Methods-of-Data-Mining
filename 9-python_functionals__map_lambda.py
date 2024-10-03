cube = lambda x: x**3# complete the lambda function 


def fibonacci(n):
    
    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    base = [0, 1]
    
    while n > 2:
        tmp = base[-1] + base[-2]
        base.append(tmp)
        n-=1
    return base
    # return a list of fibonacci numbers

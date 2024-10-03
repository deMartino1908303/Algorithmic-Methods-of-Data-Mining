# i do not understand what the solution is and this does not feel like it but it passes the tests

def wrapper(f):
    def fun(l):
        # complete the function
        def ceck_len(x):
            if len(x) > 10 and x.startswith("91"):
                x = x[2:]
            elif len(x) > 10 and x.startswith("0"):
                x = x[1:]
            elif len(x) > 10 and x.startswith("+91"):
                x = x[3:]
            return x
        clean_num = [ceck_len(x) for x in l]
        clean_num = sorted(clean_num)
        add_stuff = lambda x : '+91 ' + x[:5] + " " + x[5:]
        
        clean_num = list(map(add_stuff, clean_num))
        print(*clean_num, sep="\n")
            
        
    return fun

@wrapper

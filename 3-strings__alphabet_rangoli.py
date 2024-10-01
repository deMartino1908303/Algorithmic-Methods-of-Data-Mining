def print_rangoli(size):
    # your code goes here
    alph = 'zyxwvutsrqponmlkjihgfedcba'
    starting_point = len(alph) - size
    alph_need = alph[starting_point:]
    width = ((size*2)-1) + ((size * 2) - 2)
    for i in range(1, size+1):
        what = alph_need[0:i]+ (alph_need[0:i-1])[::-1]
        what = "-".join(list(what))
        print("{lett:-^{tag}}".format(lett=what, tag=width))
    for i in range(size-1, 0, -1):
        what = alph_need[0:i]+ (alph_need[0:i-1])[::-1]
        what = "-".join(list(what))
        print("{lett:-^{tag}}".format(lett=what, tag=width))

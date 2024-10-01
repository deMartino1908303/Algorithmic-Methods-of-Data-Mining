def print_formatted(number):
    # your code goes here
    wdt = len(bin(number)[2:])
    for i in range(1, number+1):
        otto, sedici, bipbup = oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]
        print('{0:>{wdt}} {1:>{wdt}} {2:>{wdt}} {3:>{wdt}}'.format(i, otto, sedici, bipbup, wdt = wdt) )
if __name__ == '__main__':

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()
target = input()
matching = True
not_safe = True
i = 0
while matching:
    try:
        bingo = re.search(target, string)
        string = string[int(bingo.start())+1:]
        not_safe = False
        print(f"({bingo.start()+i}, {bingo.end()-1+i})")
        i += int(bingo.start())+1
    except:
        if not_safe:
            print("(-1, -1)")
        matching = False

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

string = input()

mat = re.findall(r"([a-z0-9])\1+", string)
if len(mat) == 0:
    print("-1")
else:
    print(mat[0])

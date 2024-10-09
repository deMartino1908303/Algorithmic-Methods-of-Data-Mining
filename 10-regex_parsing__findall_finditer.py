# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()

pattern = r"(?=([^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU]))"

match = re.findall(pattern, string)

if len(match) == 0:
    print("-1")
else:
    for char in match:
        print(char[1:-1])

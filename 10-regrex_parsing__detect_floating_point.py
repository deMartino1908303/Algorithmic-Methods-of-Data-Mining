# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
iterable = int(input())

while iterable > 0:
    string = input()
    iterable -=1
    
    if not re.match(r"[\+\-\.\d]", string):
        print("False")
        continue
        
    elif len(re.findall(r"\.", string)) > 1:
        print("False")
        continue
        
    elif len(string.split(".")) != 2:
        print("False")
        continue
        
    try:
        string = float(string)
        print("True")
    except:
        print("False")
        

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def and_cahnge(match):
    return " and "

def or_cahnge(match):
    return " or "

iterator = int(input())
and_pattern = r"(\s\&{2}\s)"
or_pattern = r"(\s\|{2}\s)"

while iterator > 0:
    
    String = input()
    ceck = True

    String = re.sub(and_pattern, and_cahnge, String)
    String = re.sub(or_pattern, or_cahnge, String)
    
    String = re.sub(and_pattern, and_cahnge, String)
    String = re.sub(or_pattern, or_cahnge, String)

    print(String)
    iterator -=1

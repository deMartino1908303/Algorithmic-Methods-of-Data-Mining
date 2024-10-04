# Enter your code here. Read input from STDIN. Print output to STDOUT

string = sorted(input())

qui = [char for char in string if char.islower()]
quo = [char for char in string if char.isupper()]
qua = [char for char in string if char.isnumeric()]

even_num =[char for char in qua if int(char) % 2==0]
odd_num = [char for char in qua if char not in even_num]

print("".join(qui+quo+odd_num+even_num))

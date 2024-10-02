# Enter your code here. Read input from STDIN. Print output to STDOUT
#this code is the same of the intersection i copy pasted it from myself as the task is the same

trash_1, eng_news, trash_2, fren_news = input(), input().split(), input(), input().split()

eng_news = set(map(int, eng_news))
fren_news = set(map(int, fren_news))

print(len(eng_news.difference(fren_news)))

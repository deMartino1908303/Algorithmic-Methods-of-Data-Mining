# Enter your code here. Read input from STDIN. Print output to STDOUT

trash_1, eng_news, trash_2, fren_news = input(), input().split(), input(), input().split()

eng_news = set(map(int, eng_news))
fren_news = set(map(int, fren_news))

print(len(eng_news.intersection(fren_news)))

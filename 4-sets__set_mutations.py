# Enter your code here. Read input from STDIN. Print output to STDOUT
# i liked this one because even though symmetric differece and difference are simialr by removing symmetric in the if chain the problem does not manifest
trash, work, iterable = input(), input().split(), int(input())

work = set(map(int, work))

while iterable > 0:
    job, job_set = input(), set(map(int, input().split()))
    if "in" in job:
        work.intersection_update(job_set)
    elif "sy" in job:
        work.symmetric_difference_update(job_set)
    elif "ere" in job:
        work.difference_update(job_set)
    else:
        work.update(job_set)
    
    iterable -= 1
print(sum(work))

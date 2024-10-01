def count_substring(string, sub_string):
    counter = 0
    for i in range(0, (len(string)- len(sub_string)+1)):
        top_bound = i + len(sub_string)
        exam = string[i: top_bound]
        #print(exam)
        if sub_string == exam:
            counter += 1
        
    return counter

if __name__ == '__main__':

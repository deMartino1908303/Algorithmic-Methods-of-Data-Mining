def average(array):
    # your code goes here
    
    array = set(array)
    
    return round((sum(array)/len(array)), 3)

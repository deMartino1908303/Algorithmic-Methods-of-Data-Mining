def fun(s):
    # return True if s is a valid email, else return False
    import re
    pattern = r'^[a-zA-Z0-9_%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{1,3}$'
    
    # Use regex to check if the email matches the pattern
    if re.match(pattern, s):
        return True
    else:
        return False

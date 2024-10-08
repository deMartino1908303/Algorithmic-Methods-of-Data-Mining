#!/bin/python3

import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    
    time_format = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)

    return str(abs(int((t1 - t2).total_seconds())))

if __name__ == '__main__':

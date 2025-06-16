#!/bin/python3

import os
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'  # Format with timezone
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    delta = abs((dt1 - dt2).total_seconds())  # Get absolute difference in seconds
    return str(int(delta))  # Return as string to write it to file

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # For HackerRank-style testing

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()

#17th June, 2025, Tuesday, 12:07 am

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    '''
    A product is advertised to exactly 5 people on the
    first day of launch.

    At the end of the day, half of the people who see
    the ad like it and share it to 3 more people. This
    repeats over n days. Assume the same person does
    not see the ad twice.

    input:
    n       int     the number of days

    constraints:
    1 <= n <= 50

    output:
    print number of people who like the advertisement
    during the first n days
    '''
    shared = 5
    cumulative_likes = 0
    
    for _ in range(1, n+1):
        liked = math.floor(shared/2)
        cumulative_likes += liked

        shared = 3 * liked
    
    return cumulative_likes

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    n=50
    result = viralAdvertising(n)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    '''
    String s of fixed length can be repeated infinitely many times.
    This functions looks at the first n characters in the repeated
    string s and counts how many time the letter 'a' occurs in the
    string.

    inputs:
    s   str     a repeatable substring
    n   int     the number of characters within which 'a' is searched

    constraints:
    1 <= len(s) <= 100
    1 <= n <= 10^12

    outputs:
    The number of times the character 'a' appears in the string.

    notes:
    Only the number of occurrences in the substring s needs to be know
    since it is repeated as many times as required by n. Therefore,
    the number of times s is repeated and whether the last repetition
    of s is partial is what needs to be calculated.
    '''
    len_s = len(s)
    k = n // len_s
    k_rem = n % len_s
    # count number of 'a' in s
    a = sum([1 for i in s if i == 'a'])
    # count number of 'a' in a remainder string if there is one
    if k_rem > 0:
        a_rem = sum([1 for i in s[:k_rem] if i == 'a'])
    else:
        a_rem = 0

    return k*a + a_rem


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

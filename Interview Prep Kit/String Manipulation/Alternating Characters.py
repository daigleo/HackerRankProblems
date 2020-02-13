#!/bin/python3

import os


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_strings = int(input())

    for _ in range(num_strings):
        string = input()
        
        current = string[0]
        count = 0
        for char in string[1:]:
            if char == current:
                count += 1
            else:
                current = char

        fptr.write(str(count) + '\n')

    fptr.close()
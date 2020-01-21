def hourglassSum(arr):
    '''
    Calculates all hourglass sums and return the largest.

    input: an array arr[i][j]

    constraints:    0<= i, j <= 5
                    -9 <= arr[i][j] <= 9
    
    output: print the largest hourglass sum.    
    '''
    i_max, j_max = len(arr), len(arr[0])
    max_sum = None

    for i in range(i_max - 2):
        for j in range(j_max - 2):
            current_sum = 0
            for a in range(3):
                for b in range(3):
                    if a == 1 and (b == 0 or b == 2):
                        continue
                    else:
                        current_sum += arr[i+a][j+b]
            if max_sum is None or current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum



if __name__ == '__main__':
    test_matrix= [[1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0],
                  [1, 1, 1, 0, 0, 0],
                  [0, 0, 2, 4, 4, 0],
                  [0, 0, 0, 2, 0, 0],
                  [0, 0, 1, 2, 4, 0]
    ]

max_hourglass = hourglassSum(test_matrix)
print(f'\nThe maximum hourglass sum is: {max_hourglass}\n\n')
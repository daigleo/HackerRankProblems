def minimumSwaps(arr):
    '''
    Counts the minimum number of swaps required to sort an array.

    assumptions:
    n = len(arr)
    arr cotains all integers in interval [1, n]
    '''
    arr = [a - 1 for a in arr]
    i = 0
    swaps = 0

    while i < len(arr) - 1:
        if arr[i] != i:
            j = arr[i]
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
        else:
            i += 1
    return swaps
    
if __name__ == '__main__':
    xs = [[7, 1, 3, 2, 4, 5, 6],
          [2, 3, 4, 1, 5],
          [1, 3, 5, 2, 4, 6, 7]]

    for x in xs:
        print(f'A minimum of {minimumSwaps(x)} swaps are required to sort {x}.')

def minimumAbsoluteDifference(arr):
    '''
    Find the minimum absolute difference between two values in the array.
    min(|arr[i] - arr[j]|), where i /= j

    constraints:
    2 <= n <= 10e5
    -10e9 <= arr[i] <= 10e9
    '''
    n = len(arr)
    best = None
    for i in range(n):
        for j in range(i+1, n):
            current = arr[i] - arr[j]
            if current < 0:
                current = -1 * current
            if best is None or current < best:
                best = current
    return best

if __name__ == "__main__":
    tests = [[3, -7, 0]
            ,[-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
            ,[1, -3, 71, 68, 17]
            ]
    answers = [3, 1, 3]

    for test, answer in zip(tests, answers):
        result = minimumAbsoluteDifference(test)
        print(result == answer)
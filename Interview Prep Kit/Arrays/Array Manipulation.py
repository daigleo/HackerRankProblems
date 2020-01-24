import os


def arrayManipulation(n, queries):
    '''
    Given a 1-indexed array of zeroes of length n. A list of queries is provided
    such that each query is given as (a, b, k), where a is a start index, b
    an end index, and k is the amount to add to each index in the range [a, b].

    constraints:
    3 <= n <= 1e7
    1 <= len(queries) <= 2e5
    1 <= a <= b <= n
    0 <= k <= 1e9

    https://codereview.stackexchange.com/questions/95755/algorithmic-crush-problem-hitting-timeout-errors

    Note: The below code works but must be submitted as Pypy 3 instead of Python 3
    to valide on Hacker Rank... I'm not sure why that is.
    '''
    arr = [0] * (n + 2)
    for a, b, k in queries:
        arr[a] += k
        arr[b+1] -= k
    max_value = arr[1]
    for i in range(2, n+2):
        arr[i] +=  arr[i-1]
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value


def works_but_too_slow(n, queries):
    arr = [0] * n
    print(arr)
    for a, b, k in queries:
        for i in range(a-1, b):
            arr[i] += k
    return max(arr)


if __name__ == '__main__':
    queries = [[1, 5, 3],
               [4, 8, 7],
               [6, 9, 1]
    ]

    results = arrayManipulation(10, queries)
    print(results)

    queries = [[1, 2, 100],
               [2, 5, 100], 
               [3, 4, 100],
               [4, 5, 50]
    ]

    results = arrayManipulation(5, queries)
    print(results)

    n = 15
    queries = [[1, 15, 200],
               [5, 15, 200],
               [14, 15, 200],
               [10, 15, 150],
               [15, 15, 50]]
    results = arrayManipulation(n, queries)
    print(results)

    n = 15
    queries = [[1, 10, 20000],
               [1, 5, 20000],
               [1, 3, 20000],
               [1, 2, 15000],
               [1, 1, 50000]]
    results = arrayManipulation(n, queries)
    print(results)

    # input07.txt is a text case downloaded from hacker rank
    ans = 2497169732
    fname = os.path.join(os.getcwd(), 'Interview Prep Kit', 'Arrays', 'input07.txt')
    with open(fname, 'r') as f:
        n, m = map(int, f.readline().strip().split())
        queries = []
        for _ in range(m):
            queries.append(list(map(int, f.readline().strip().split())))
    
    results = arrayManipulation(n, queries)
    print(results == ans)
    print(f'{results}: {ans}')

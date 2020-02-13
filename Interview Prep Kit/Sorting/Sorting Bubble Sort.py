def countSwaps(a):
    n = len(a)
    swap_count = 0

    # Code provided by Hacker Rank
    # I'm not convinced this should be a problem.
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap_count += 1
    
    print(f'Array is sorted in {swap_count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
import time
from functools import wraps


def timed_func(fn, n=1000000):
    @wraps(fn)
    def do_n_times(*args, **kwargs):
        time_start = time.perf_counter()
        for _ in range(n):
            result = fn(*args, **kwargs)
        time_elapsed = time.perf_counter() - time_start
        print(f'{fn.__name__}: {time_elapsed:0.2f} s')
        return result
    return do_n_times


def maxMin(k, arr):
    '''
    Given an array, construct a subarray of a given length such that its
    unfairness is minimized. The unfairness is calculated by 
    max(subarr) - min(subarr)
    
    inputs:
    arr     an array of length n
    k       the desired length of the subarray

    constraints:
    2 <= n <= 10e5,
    2 <= k <= n,
    0 <= arr[i] <= 10e9

    return the smallest unfairness

    NOTE: Assuming k=2, sorting the array minimizes the unfairness between
          consecutive values. This holds for k > 2 since their position is
          such that it minimizes their difference. Thus, sorting the array
          and looking at each first and last value of the window should
          solve the problem.
    '''
    sorted_arr = sorted(arr)
    print(sorted_arr)
    lowest_unfairness = None
    for min_val, max_val in zip(sorted_arr[:-k+1], sorted_arr[k-1:]):
        unfairness = max_val - min_val
        print(f'\t[{min_val} ... {max_val}], {unfairness}/{lowest_unfairness}')
        if lowest_unfairness is None:
            lowest_unfairness = unfairness
        elif unfairness < lowest_unfairness:
            lowest_unfairness = unfairness
        if unfairness == 0:
            return 0
    return lowest_unfairness

def maxMin2(k, arr):
    '''
    A more compact form of the above, although this one is less efficient.
    Most likely because calling calling min() after the list comprehension
    is an extra loop through an array whilst the other function does the
    equivalent min() during the list building.
    '''
    sorted_arr = sorted(arr)
    diffs = [i_max - i_min for i_max, i_min 
                            in zip(sorted_arr[k-1:], sorted_arr[:-k])]
    return min(diffs)
        



if __name__ == "__main__":
    ks = [3, 4, 2, 3]
    answers = [20, 3, 0, 2]
    arrays =[[10, 100, 300, 200, 1000, 20, 30]
            ,[1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
            ,[1, 2, 1, 2, 1]
            ,[100, 200, 300, 350, 400, 401, 402]
    ]

    for k, array, answer in zip(ks, arrays, answers):
        result = maxMin(k, array)
        print(result, result == answer)
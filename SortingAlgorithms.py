import time
from functools import wraps


def timed_func(fn, n=1000):
    @wraps(fn)
    def do_n_times(*args, **kwargs):
        time_start = time.perf_counter()
        for _ in range(n):
            result = fn(*args, **kwargs)
        time_elapsed = time.perf_counter() - time_start
        print(f'{fn.__name__}: {time_elapsed:0.2f} s')
        return result
    return do_n_times


# https://en.wikipedia.org/wiki/Sorting_algorithm


def quick_sort():
    # https://en.wikipedia.org/wiki/Quicksort
    pass


def bubble_sort(arr):
    # https://en.wikipedia.org/wiki/Bubble_sort
    swapped = True
    n = len(arr)
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
    return arr


def insertion_sort():
    # https://en.wikipedia.org/wiki/Insertion_sort
    pass


def heap_sort():
    # https://en.wikipedia.org/wiki/Heapsort
    pass


def counting_sort(arr):
    # https://en.wikipedia.org/wiki/Counting_sort
    # Knowing the range of arr would speed up this algorithm as it would
    # avoid the extra pass through the array to determine the min/max values
    arr_min, arr_max = None, None
    for item in arr:
        if arr_min is None or item < arr_min:
            arr_min = item
        if arr_max is None or item > arr_max:
            arr_max = item

    freqs = (arr_max - arr_min + 1) * [0]
    for item in arr:
        freqs[item - arr_min] += 1
    for i in range(1, len(freqs)):
        freqs[i] = freqs[i-1] + freqs[i]
    freqs = [0] + freqs[:-1]

    sorted_arr = len(arr) * [None]
    for item in arr:
        sorted_arr[freqs[item - arr_min]] = item
        freqs[item - arr_min] += 1
    return sorted_arr

def radix_sort(arr):
    # https://en.wikipedia.org/wiki/Radix_sort#Least_significant_digit_radix_sorts
    pass


def merge_sort(arr):
    # https://en.wikipedia.org/wiki/Merge_sort
    n = len(arr)
    if n < 2:
        return arr
    mid = n // 2 + n % 2
    L, R = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    i = j = 0
    n, m = len(L), len(R)
    merged_arr = []
    while i < n and j < m:
        if L[i] <= R[j]:
            merged_arr.append(L[i])
            i += 1
        else:
            merged_arr.append(R[j])
            j += 1
    while i < n:
        merged_arr.append(L[i])
        i += 1
    while j < m:
        merged_arr.append(R[j])
        j += 1
    return merged_arr



def tim_sort():
    # https://en.wikipedia.org/wiki/Timsort
    # https://github.com/python/cpython/blob/dd754caf144009f0569dda5053465ba2accb7b4d/Objects/listsort.txt
    pass


if __name__ == "__main__":
    tests = [[56, 24, 35, 3, 100, 88, 22, 89, 12, 88, 99, 6, 73]]
    functions = [bubble_sort, merge_sort, counting_sort]

    for test in tests:
        for function in functions:
            print(timed_func(function, 10000)(test))

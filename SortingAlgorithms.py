import time

def timed_func(fn, n=10000):
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


def counting_sort():
    # https://en.wikipedia.org/wiki/Counting_sort
    pass


def radix_sort():
    # https://en.wikipedia.org/wiki/Radix_sort#Least_significant_digit_radix_sorts
    pass


def merge_sort():
    # https://en.wikipedia.org/wiki/Merge_sort
    pass


def tim_sort():
    # https://en.wikipedia.org/wiki/Timsort
    # https://github.com/python/cpython/blob/dd754caf144009f0569dda5053465ba2accb7b4d/Objects/listsort.txt
    pass


if __name__ == "__main__":
    tests = [[56, 24, 35, 3, 100, 88, 22, 89, 12, 88, 99, 6, 73]]

    for test in tests:
        print(bubble_sort(test))

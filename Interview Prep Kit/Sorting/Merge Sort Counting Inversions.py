'''
The goal is to determine how many inversions are required to sort an array.
An inversion is defined as two _adjacent_ indices changing positions.

The algorithm below uses a merge sort to determine the number of inversions
required. The inversions are counted when sorted sublists are merged back 
together. If an element in the right list is smaller than the left list,
at least one inversion has occurred.

A key thing is that the number of inversions is greater or equal to the
number of swaps performed during the merge sort.
'''
def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr, 0
    else:
        inversions = 0
        mid = n // 2 + n % 2
        (L, Li), (R, Ri) = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        inversions = Li + Ri
        n, m = len(L), len(R)
        i = j = 0
        sorted_arr = []
        # Merge lists
        while i < n and j < m:
            if L[i] <= R[j]:
                sorted_arr.append(L[i])
                i += 1
            else:
                inversions += n - i
                sorted_arr.append(R[j])
                j += 1
        # Collect remaining terms
        while i < n:
            sorted_arr.append(L[i])
            i += 1
        while j < m:
            sorted_arr.append(R[j])
            j += 1
        return sorted_arr, inversions


def countInversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


if __name__ == '__main__':
    tests = [[1, 1, 1, 2, 2]
            ,[2, 1, 3, 1, 2]
            ,[7, 5, 3, 1]
    ]
    answers = [0, 4, 6]

    for test, answer in zip(tests, answers):
        result = countInversions(test)
        print(result == answer)
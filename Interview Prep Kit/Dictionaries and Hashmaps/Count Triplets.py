def countTriplets(arr, r):
    '''
    Given an array of numbers and a common ratio,
    find the number of triplets following a geometric progression,
    such that arr[i] <= arr[j] <= arr[k],
              arr[j] = r * arr[i],
              arr[k] = r * r * arr[i] = r * arr[j]
              i < j < k.
    Note that, contrary to the examples given by Hacker Rank, the array
    is not necessarily sorted.

    A brute force method will time out when submitted.

    constraints:
    1 <= |arr| <= 10e5
    1 <= r <= 10e9
    1 <= arr[i] <= 10e9
    '''
    ahead = {}
    potential = {}
    triplets = 0

    for val in arr:
        val_next = r * val

        if val in potential:
            triplets += potential[val]
            
        if val in ahead:
            potential.setdefault(val_next, 0)
            potential[val_next] = potential[val_next] + ahead[val]
            
        ahead.setdefault(val_next, 0)
        ahead[val_next] += 1

    return triplets


if __name__ == '__main__':
    r = [2, 3, 5, 6, 3, 1]
    test = [[1, 2, 2, 4], 
            [1, 3, 9, 9, 27, 81],
            [1, 5, 5, 25, 125],
            [6, 216, 36, 6, 216, 36, 36, 216, 1296, 216],
            [1, 3, 3, 9, 3, 9],
            [1, 1, 1, 1, 1]
    ]
    ans = [2, 6, 4, 15, 5, 10]

for ratio, array, answer in zip(r, test, ans):
    print(answer == countTriplets(array, ratio))
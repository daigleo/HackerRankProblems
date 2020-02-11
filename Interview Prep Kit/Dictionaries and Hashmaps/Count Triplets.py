def countTriplets(arr, r):
    '''
    Given an array of numbers and a common ratio,
    find the number of numbers following a geometric progression.
    Note that, contrary to the examples given by Hacker Rank, the array
    is not necessarily sorted.

    constraints:
    1 <= |arr| <= 10e5
    1 <= r <= 10e9
    1 <= arr[i] <= 10e9
    '''
    # if r == 1:
    #     return 0

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

'''
 0    1   2  3    4   5   6    7     8    9
[6, 216, 36, 6, 216, 36, 36, 216, 1296, 216]
i[n]
0[7]: (0, 2, 4), (0, 2, 7), (0, 2, 9), (0, 5, 7), (0, 5, 9), (0, 6, 7), (0, 6, 9)
1[0]
2[2]: (2, 4, 8), (2, 7, 8)
3[4]: (3, 5, 7), (3, 5, 9), (3, 6, 7), (3, 6, 9)
4[0]
5[1]: (5, 7, 8)
6[1]: (6, 7, 8)
7[0]
----------- THERE CAN'T BE TRIPLETS PAST i > |arr| - 3
8[0]
9[0]

TOTAL: 15
'''
'''
i
0: 6    {36: 1},                            0 triplets
1: 216  {36: 1, 1296: 1},                   0 triplets
2: 36   {36: 1, 216: 1, 1296: 1}            0 triplets
3: 6    {36: 2, 216: 1, 1296: 1}            0 triplets
4: 216  {36: 2, 216: 1, 1296: 2}            1 triplet
5: 36   {36: 2, 216: 2, 1296: 2}            1 triplet
6: 36   {36: 2, 216:, 3, 1296: 2}           1 triplet
7: 216  {36: 2, 216: 3, 1296: 3}            5 triplets
8: 1296 {36: 2, 216: 3, 1296: 3, 7776: 1}   15 triplets
9

for num in nums:
    check if num in demand (ahead[num] > 0)
        if True -> there is a num / r before it
    check if r * num in demand 
'''

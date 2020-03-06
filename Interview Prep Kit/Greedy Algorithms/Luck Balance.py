def luckBalance(k, contests):
    '''
    If Lena wins a contest, her luck goes down; if she loses a contest,
    her luck goes up. Lena wants to win an upcoming competition but first
    has to participate in a number of preliminary contests. Some of the
    preliminary contests are important, some are not. She must win a minimum
    number of important preliminary contests to get in the competition. Given
    the number of important contests she must win and the luck value and impor-
    tance of the preliminary contests, what is the maximum luck that Lena can
    have when entering the upcoming competition.

    inputs:
    k           the number of preliminary contests Lena must win
    contests    a list of lists with preliminary contest information, s.t.
        [0]     the luck value of the contest
        [1]     1 if the contest is important, 0 if it is not

    constraints:
    1 <= number of contests <= 100
    0 <= k <= number of important contests
    1 <= contests[0] <= 10e4
    important = {0, 1}
    '''
    contests = sorted(contests, key=lambda x: x[0], reverse=True)
    luck_balance = 0
    for luck, important in contests:
        if k > 0 or not important:
            if important:
                k -= 1
            luck_balance += luck
        else:
            luck_balance -= luck
    return luck_balance


if __name__ == "__main__":
    tests = [[(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
            ,[(5, 1), (1, 1), (4, 0)]
            ,[(5, 1), (1, 1), (4, 0)]
    ]
    ks = [3, 2, 1]
    answers = [29, 10, 8]

    for test, k, answer in zip(tests, ks, answers):
        print(luckBalance(k, test) == answer)
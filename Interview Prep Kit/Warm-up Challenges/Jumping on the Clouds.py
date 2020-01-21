def jumpingOnClouds(c):
    '''
    Input is list c containing 0s & 1s. Zeroes are 'safe' clouds
    and ones are 'danger' clouds. The goal is to traverse from
    cloud index 0 to cloud index n (n=len(c) - 1) by jumping from
    cloud to cloud in the shortest number of jumps possible.
    There are only two rules: a jump can only be
    from clouds one or two indices further than the current cloud.
    I.e., if i=2, the next cloud can only be i=3 or i=4. A jump
    cannot be made to a danger cloud.

    constraints:
    2 <= n <= 100
    c[i] = {0, 1}
    c[0] = c[n-1] = 0
    '''
    if len(c) <= 3:
        return 1
    else:
        if c[2] == 0:
            return jumpingOnClouds(c[2:]) + 1
        else:
            return jumpingOnClouds(c[1:]) + 1

if __name__ == '__main__':
    print('test case one.')
    n = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
    print(f'It took {n} jumps.')
    print('\ntest case two.')
    n = jumpingOnClouds([0, 0, 0, 0, 1, 0])
    print(f'it took {n} jumps.')

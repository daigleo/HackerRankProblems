def rotLeft(a, d):
    '''
    Performs d left array rotations on array a
    inputs:
    a   an array
    d   the number of left rotations to perform on a
    
    constraints:
    1 <= len(a) <= 10e5
    1 <= d <= len(a)
    1 <= a[i] <= 10e6
    
    output:
    the rotated array
    '''
    return a[d:] + a[:d]

def with_modular_math(a, d):
    '''
    Solution using modular math found in the problem discussions.
    '''
    n = len(a)
    b = n*[None]
    for i in range(n):
        b[(n-d+i) % n] = a[i]

    return b


if __name__ == '__main__':

    d = 4
    a = [1, 2, 3, 4, 5]
    a_check = rotLeft(a, d)
    a_ans = [5, 1, 2, 3, 4]

    a_check = with_modular_math(a, d)
    print(a_check)
    print(a_check == a_ans)

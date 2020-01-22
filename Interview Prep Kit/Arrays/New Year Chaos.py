def minimumBribes(q):
    '''
    A queue of people is such that each person entering the queue is labeled
    with a number corresponding with the number of people in the queue. Any
    person can bribe the person in front to swap position. This bribe can
    occur twice for each person.

    Given the end-state of a queue, what is the minimum number of bribes
    required to achieve this state.

    input:
    q   a queue of length n that has been reordered
        assume q[0] is the front of the queue.

    output:
    the minimum number of bribes required to achieve the status, or the string
    'Too chaotic' if the queue state is not possible.

    constraints:
    1 <= len(q) <= 10e5

    link to problem:
    https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    '''
    # Count number of bribes taken by any given person
    # i.e., count number of people with larger number between them (i)
    # and their starting position (qi)
    total_bribes = 0
    for i, qi in enumerate(q):
        if qi - (i + 1) > 2:
            print('Too chaotic')
            return
        # for person in q[max(qi-2, 0):i]:
        for person in q[max(qi-2, 0):i]:
            if person > qi:
                total_bribes += 1
    print(total_bribes)

def minimumBribes2(q):
    bribes = 0
    swap = True
    q = [(p, 0) for p in q]

    while swap:
        swap = False
        for i in range(len(q)-1):
            if q[i][0] > q[i+1][0]:
                q[i] = (q[i][0], q[i][1]+1)
                if q[i][1] > 2:
                    print('Too chaotic')
                    return
                q[i], q[i+1] = q[i+1], q[i]
                swap = True
                bribes += 1
    print(bribes)



if __name__ == '__main__':
    q0 = [1, 2, 3, 4, 5]
    q1 = [2, 1, 5, 3, 4]
    q2 = [2, 5, 1, 3, 4]
    q3 = [3, 4, 5, 2, 1]
    q4 = [3, 2, 1, 6, 4, 8, 5, 9, 7]
    q5 = [3, 2, 6, 1, 4, 8, 5, 9, 7]
    q6 = [3, 1, 5, 2, 7, 8, 4, 10, 9, 6]
    q7 = [3, 4, 5, 1, 2]

    qx = q6

    print(list(range(1,len(qx)+1)))
    print(qx)
    minimumBribes(qx)
    minimumBribes2(qx)

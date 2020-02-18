def is_special_palindrome(s):
    n = len(s)
    m = n // 2
    ch = s[0]
    for i in range(m):
        if s[i] != s[n-i-1] or s[i] != ch or s[n-i-1] != ch:
            return False
    return True

def substrCount(L, s):
    count = L
    for num_subs in range(1, L):
        subs = [s[i:i + L - num_subs + 1] for i in range(num_subs)]
        count += sum(map(is_special_palindrome, subs))
    return count


if __name__ == '__main__':
    tests = ['asasd', 'abcbaba','aaaa', '']
    ans = [7, 10, 10, 0]

    for test, an in zip(tests, ans):
        res = substrCount(len(test), test)
        print(f'{test}: {res}|{an}')

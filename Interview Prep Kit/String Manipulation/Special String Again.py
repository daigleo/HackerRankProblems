def substrCount(n, s):
    '''
    This function needs to count the number of substrings that are special
    palindromes. A special palindrome is either:
    1. all the same characters ('aaaaa'); or
    2. all the same characters except for the middle character ('aabaa').

    A single character is considered a palindrome. Therefore, the minimum
    answer returned by this function is the length of the string n.

    constraints:
    n <= 10e6
    '''
    count = n
    
    for i in range(n):
        # Check for special palindromes with all same letters e.g., 'aaaa'
        for j in range(i+1, n):
            if s[i] != s[j]:
                break
            count += 1
        # check for special palindromes with different middle character
        # surrounded by all same letters e.g., 'aaabaaa'
        if i > 0 and s[i-1] != s[i]:
            alt_char = s[i-1]
            for j in range(1, min(i+1, n-i)):
                if s[i-j] != alt_char or s[i+j] != alt_char:
                    break
                count += 1
    return count


if __name__ == '__main__':
    tests = ['asasd', 'abcbaba','aaaa', '', 'aaaaaaa', 'aabaaaa']
    ans = [7, 10, 10, 0, 28, 16]

    for test, an in zip(tests, ans):
        res = substrCount(len(test), test)
        print(f'{test}: {res}|{an}')

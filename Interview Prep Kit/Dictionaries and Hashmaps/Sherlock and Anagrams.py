def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

# Note: I was initially using the above function as n choose k, but since
# n choose k = n!/[2!(n-k)!] = 1x2x3x...xn/[2(1x2x3x...xn-2)]
#            = (n-1)n/2
# we can simply replace the call to choose(n, k) with (n-1)n/2
def sherlockAndAnagrams(s):
    L = len(s)
    freq = {}

    for sub_len in range(1, L):
        for i in range(L - sub_len + 1):
            substr = s[i:i+sub_len]
            substr = ''.join(sorted(substr))
            freq.setdefault(substr, 0)
            freq[substr] += 1
    print(freq)

    anagrams = 0
    for value in freq.values():
        if value > 1:
            anagrams += value * (value - 1) // 2

    return anagrams


if __name__ == '__main__':
    words = ['abba', 'abcd', 'ifailuhkqq', 'kkkk', 'cdcd']

    for word in words:
        print(word)
        print(sherlockAndAnagrams(word))

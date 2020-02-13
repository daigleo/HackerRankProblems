def makeAnagram(a, b):
    '''
    Two strings a and b need to be modified to form an anagram. This functions
    determines the minimum number of characters that need to be removed
    for the strings to be anagrams. |a| may be different to |b|.

    constraints:
    1 <= |a|, |b| <= 10e4
    a, b elem[a-z]

    ord(char) returns decimal value of char
    '''
    a = sorted(a)
    b = sorted(b)
    lena = len(a)
    lenb = len(b)

    matches = 0
    i = j = 0

    while i < lena and j < lenb:
        if a[i] == b[j]:
            matches += 1
            i += 1
            j += 1
        else:
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
    return lena + lenb - 2 * matches


if __name__ == '__main__':
    a, b = 'cinema', 'changes'
    ans = 4
    print(makeAnagram(a, b))


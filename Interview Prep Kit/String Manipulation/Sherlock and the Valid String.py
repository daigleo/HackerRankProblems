def isValid(s):
    '''
    This function checks if a string is valid. A string is considered valid if:
        i) all the letters in the string occur at the same frequency, or
        ii) condition i) is true if one character is removed.
    '''
    s = sorted(s)
    s.append(' ')
    freq = None
    cur_freq = 1
    removed = False
    previous = s[0]
    for current in s[1:]:
        if current != previous:
            # First letter checked
            if freq is None:
                freq = cur_freq
            # Remove letter. If more than one to be removed, not a valid string
            elif cur_freq != freq:
                if not removed and (cur_freq == 1 or abs(cur_freq - freq) == 1):
                    removed = True
                else:
                    return 'NO'
            cur_freq = 1
            previous = current
        else:
            cur_freq += 1
    return 'YES'

if __name__ == '__main__':
    tests = ['aabbcd', 'aabbccddeefghi', 'abcdefghhgfedecba', 'abcabcabcabcabc', 'becbecbecfbec',
             'becfbecbecfbec', 'befcfbecbfecfbec', 'befcfbecbfecfbecff']
    expected_results = ['NO', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES', 'NO']

    for test, expected_result in zip(tests, expected_results):
        print(isValid(test) == expected_result)
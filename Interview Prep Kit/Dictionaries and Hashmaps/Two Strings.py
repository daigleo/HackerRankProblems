'''
    Given two strings, determine if they share a common substring.
    Note:   The problem definition states that two words sharing a letter
            means that they share a substring.
    
    returns: YES or NO

    create a dictionary of letters for s1 and match each letter of s2 to s1.
    If there are __any__ matches, return YES. Otherwise, return NO.
    '''

# If strictly using a hashtable/dictionary:
def twoStrings(s1, s2):
    s1 = {char:char for char in s1}

    for char in s2:
        try:
            s1[char]
            return 'YES'
        except:
            continue
    return 'NO'

# when using sets (this is quicker)
def twoStrings2(s1, s2):
    if set(s1).intersection(set(s2)):
        return 'YES'
    else:
        return 'NO'

print(twoStrings('hello','world'))
print(twoStrings('hi', 'bye'))
    
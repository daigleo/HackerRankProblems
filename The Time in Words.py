def timeInWords(h, m):
    '''
    Given an input containing the time in hours and minutes,
    this function returns a string containing the time in words.
    e.g.,   3:00 -> three o' clock
            7:15 -> quarter past seven
            8:30 -> half past eight
            12:45 -> quarter to twelve
            1:12 -> twelve minutes past one
            4:40 -> twenty minutes to five
            etc.
    inputs:
    h   the hours    1 <= h <= 12
    m   the minutes  0 <= m < 60

    returns:
    the time in words
    '''
    def minutes(m):
        if m == 1:
            return ' minute'
        if m == 15 or m == 30:
            return ''
        else:
            return ' minutes'
    
    numbers = { 1:'one', 2:'two', 3:'three',4:'four',5:'five',
                6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
                11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
                15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen',
                19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two',
                23:'twenty three', 24:'twenty four', 25:'twenty five',
                26:'twenty six', 27:'twenty seven', 28:'twenty eight',
                29:'twenty nine', 30:'half'}
    h = int(h)
    m = int(m)

    if m == 0:
        return numbers[h] + ' o\' clock'
    elif m > 0 and m <= 30:
        return numbers[m] + minutes(m) + ' past ' + numbers[h]
    else:
        if h+1 > 12:
            h = 0
        m = 60 - m
        return numbers[m] + minutes(m) + ' to ' + numbers[h+1]

if __name__ == '__main__':
    test_times = ['3:00', '7:15', '8:30', '12:45', '1:12', '4:40', '6:56', '11:00', '1:22', '5:47', '2:59', '2:01']

    for time in test_times:
        h,m = time.split(':')
        print(time, end='\t')
        print(timeInWords(h, m))
        
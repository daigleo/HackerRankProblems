def checkMagazine(magazine, note):
    mag_count  = {}

    for word in magazine:
        try:
            mag_count[word] += 1
        except:
            mag_count[word] = 1

    for word in note:
        try:
            if mag_count[word] == 0:
                print('No')
                return
            mag_count[word] -= 1
        except:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    ran = ['two', 'times', 'two', 'is', 'four']

    # returns No
    mag = ['two', 'times', 'three', 'is', 'not', 'four']
    checkMagazine(mag, ran)
    # returns Yes
    mag = ['two', 'times', 'three', 'is', 'not', 'four', 'two']
    checkMagazine(mag, ran)
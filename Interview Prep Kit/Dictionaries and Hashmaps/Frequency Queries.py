def freqQuery(queries):
    array = {}
    freq = {}
    checks = []

    def update_dict(_dict, key, x):
        if key in _dict:
            curr = _dict[key]
            _dict[key] = [0, curr+x][curr+x > 0]
        else:
            _dict[key] = [0, x][x > 0]
        return _dict

    for code, val in queries:
        if code == 3:
            if val in freq:
                checks.append([0, 1][freq[val] >= 1])
            else:
                checks.append(0)
        else:
            op = [-1, 1][code == 1]
            if val in array:
                freq = update_dict(freq, array[val], -1)
            array = update_dict(array, val, op)
            freq = update_dict(freq, array[val], 1)
    
    return checks

if __name__ == '__main__':
    queries = [(1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2)]
    print(freqQuery(queries))

    queries = [(3, 4), (2, 1003), (1, 16), (3, 1)]
    print(freqQuery(queries))

    queries = [(1, 3), (2, 3), (3, 2), (1, 4), (1, 5), (1, 5), (1, 4), 
               (3, 2), (2, 4), (3, 2)]
    print(freqQuery(queries))
    


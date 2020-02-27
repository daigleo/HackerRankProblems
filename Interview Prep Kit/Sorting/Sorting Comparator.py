from functools import cmp_to_key


class Player:
    '''
    Build a comparator function in the Player class such that players are
    sorted in descending order based on their score. If two players have the
    same score, sort them alphabetically.

    constraints:
    0 <= score <= 1000
    Players can have the same name
    Player names are lower case English alphabet
    '''
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f'{self.name}: {self.score}'

    @staticmethod
    def comparator(a, b):
        '''
        returns:
        -1 if a < b
         0 if a = b
         1 if a > b

         Note: -1 indicates that a appears before b,
                1 indicates that a appears after b,
                0 indicates that a and b are the same.
                Therefore, comparator(a, b) can be used to influence the
                results of a function that uses a key (e.g., sorted, min, max).
        '''
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        if a.name > b.name:
            return 1
        if a.name < b.name:
            return -1
        return 0


if __name__ == '__main__':
    test = [Player('amy', 100), 
            Player('david', 100),
            Player('david', 100),
            Player('david', 100),
            Player('heraldo', 50),
            Player('aakansha', 75),
            Player('aleksa', 150)
        ]
    test = sorted(test, key=cmp_to_key(Player.comparator))
    for item in test:
        print(item)
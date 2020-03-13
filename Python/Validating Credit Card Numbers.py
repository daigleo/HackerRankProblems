import re


def check_cc(num):
    # does the number start with a 4, 5, or 6 and
    # is the number 16 digits long or 16 digits + 3 hyphens
    if not(re.match(r'[456]\d{15}$', num) or 
           re.match(r'[456]\d{3}-\d{4}-\d{4}-\d{4}$', num)):
        return 'Invalid'
    # Checks if four of the same numbers in a row.
    # Needs to remove hyphens before the check.
    if re.search(r'((\d)\2{3})', re.sub('-', '', num)):
        return 'Invalid'
    return 'Valid'

def check_cc2(num):
    if re.match(r'(?!.*(\d)(-?\1){3})[456](?:\d){3}(?:-?\d{4}){3}$', num):
        return 'Valid'
    return 'Invalid'

    
if __name__ == '__main__':
    # ccs = [input().strip() for _ in range(int(input()))]
    ccs = ['4123456789123456', 
           '5123-4567-8912-3456', 
           '61234-567-8912-3456', 
           '4123356789123456', 
           '5133-3367-8912-3456', 
           '5123 - 3567 - 8912 - 3456'
    ]
    answers = ['Valid', 'Valid', 'Invalid', 'Valid', 'Invalid', 'Invalid']
    results = map(check_cc, ccs)
    for answer, result in zip(answers, results):
        print(answer == result)
    results = map(check_cc2, ccs)
    for answer, result in zip(answers, results):
        print(answer == result)
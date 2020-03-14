import re
    

def validate_postal_code(postal_code):
    return bool(re.match(r'[1-9]\d{5}$', postal_code)
            and len(re.findall(r'(\d)(?=.\1)', postal_code)) < 2
            )


if __name__ == "__main__":
    postal_codes = ['121426', '523563', '552523', '110000']
    answers = [True, True, False, False]

    for postal_code, answer in zip(postal_codes, answers):
        print(validate_postal_code(postal_code) == answer)
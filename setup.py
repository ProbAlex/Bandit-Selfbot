from utils import get_tokens, check_token


def get_token():

    print("Selfbot")
    print('Gathering Tokens')
    count = 1
    found = {}
    for token in get_tokens():
        if token in found.values():
            continue

        a = check_token(token)

        if a != "Invalid":
            found[count] = token
            print(f"{count}. {a} | Token: {token}")
            count += 1

    if len(found) > 1:
        inp = int(input('Select account: '))
    else:
        inp = 1

    if inp not in found.keys():
        print('Invalid account')
        exit()

    token = found[inp]

    return token

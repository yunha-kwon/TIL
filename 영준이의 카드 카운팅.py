for tc in range(1, int(input())+1):
    card = input()
    check = []
    card_set = {'S': 13, 'D': 13, 'H': 13, 'C': 13}

    for i in range(0, len(card), 3):
        check.append(card[i:i+3])

    if len(check) != len(set(check)):
        print(f'#{tc} ERROR')

    else:
        for i in range(0, len(card)-2, 3):
            num = card_set[card[i]] - 1
            card_set[card[i]] = num

        print(f'#{tc}', end=' ')
        print(*card_set.values())
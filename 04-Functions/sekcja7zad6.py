def hide(card_number):
    
    first = card_number[:2]
    last = card_number[-4:]
    mask = '*' * (len(card_number) - len(first) - len(last))

    return f'{first}{mask}{last}'
     
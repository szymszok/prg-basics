def f(player1, player2):
    total_value_player1 = sum(10 if card in ['A', 'K', 'Q', 'J', 'T'] else int(card) for card in player1)
    total_value_player2 = sum(10 if card in ['A', 'K', 'Q', 'J', 'T'] else int(card) for card in player2)
    return total_value_player1 >= total_value_player2

print(f("AJ972", "AQT72"))
print(f("9532", "K8"))
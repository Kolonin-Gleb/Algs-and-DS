# Разменять купюру минимальным количеством монет


def exchange_banknote(banknote, max_to_min_coins):
    # Количество монет
    max_coin_ammount = 0
    mid_coin_ammount = 0
    min_coin_ammount = 0
    
    while(banknote >= max_to_min_coins[0]):
        banknote -= max_to_min_coins[0]
        max_coin_ammount += 1
    while(banknote >= max_to_min_coins[1]):
        banknote -= max_to_min_coins[1]
        mid_coin_ammount += 1
    while(banknote >= max_to_min_coins[2]):
        banknote -= max_to_min_coins[2]
        min_coin_ammount += 1

    return max_coin_ammount, mid_coin_ammount, min_coin_ammount

# Купюра
banknote = 167
# Монеты
max_to_min_coins = [10, 5, 2]

print(exchange_banknote(banknote, max_to_min_coins))

# ДЗ написать жадный алгоритм для интервалов или рюкзака.
# Код прислать на почту.

# Это дает 5 баллов к контрольной точке!!

# На следующшей паре КР на 30 минут
# По рекурсии и жадным алгоритмам


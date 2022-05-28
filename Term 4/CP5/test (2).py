# Я ДОЛЖЕН ОПРЕДЕЛИТЬ СТОИМОСТИ КАЖДОГО СПОСОБА ДОБРАТЬСЯ В ЗАДАННЫЕ ТОЧКИ

import math


cur_position = 0
target_position = 5
k = 3
prices = [0, -7, -5, -6, -4, 4, 2, 0]

price_to_come = [-math.inf] * (target_position - cur_position)

next_position = cur_position + 1

# Определение Лучших способов добраться в те позиции, до которых можно сразу допрыгнуть
for i in range(next_position, cur_position + k + 1): #TODO: Как быть, если k = 1?
	# Прямой способ добраться до позиции всегда самый выгодный, т.к. все предыдущие элементы < 0
	price_to_come[i - 1] = prices[i]

# Определение лучших способов добраться в удаленные позиции
for y in range(cur_position + k + 1, target_position + 1):
	# Сохраняю все стоимости добаться до позиции
	possible_prices = []
	for j in range(y-k-1, y - 1): # Рассматриваю k предыдущих цен
		possible_prices.append(price_to_come[j] + prices[y]) # TODO: Проблема с индексами prices
	price_to_come[y - 1] = max(possible_prices)

print(price_to_come)
		

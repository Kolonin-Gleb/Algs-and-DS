# Я ДОЛЖЕН ОПРЕДЕЛИТЬ СТОИМОСТИ КАЖДОГО СПОСОБА ДОБРАТЬСЯ В ЗАДАННЫЕ ТОЧКИ

import math


position = 0
target_position = 5
k = 3
prices = [0, -7, -5, -6, -4, 4, 2, 0]

price_to_come = [-math.inf] * (target_position - position)

for i in range(len(price_to_come)):
    # Если позади элементов меньше, чем возможность прыжка
    # То суммируем значения тех эл., что имеются и +1, т.к. можно допрыгнуть из тек. положения


	# Определение Лучших способов добраться в те позиции, до которых можно сразу допрыгнуть
	next_position = position + 1 # Высчитываю стоимость добраться до следующей позиции

	for i in range(position + 1, position + k):
		# Прямой способ добраться до позиции всегда самый выгодный, т.к. все предыдущие элементы < 0
		price_to_come[i] = prices[i]
		break
		#else: # Сохраняю все способы добаться до следующей позиции
		#	possible_prices = []
		#	possible_prices.append(prices[i]) # Прямой способ

		#	# Может ли быть такое, что прямой способ всегда самый выгодный?
		#	# Да, прямой ход всегда самый выгодный, т.к. если есть + число до которого можно сразу допрыгнуть, я делаю это автоматически!

		#	#for j in range(1, k)
		#	#possible_prices.append(price_to_come[i - 1])

		print(ways_to_come)
    else:
		break
		


# Число способов прийти в те элементы, до которых нельзя допрыгнуть
ways_to_come.append(0)
ways_to_come.append(0)
ways_to_come.append(0)

k = 3 # Сила прыжка
position = 3 # Элемент, до которого нужно определить лучший способ добраться

for i in range(position, len(ways_to_come)):
	# Определяем предшествующие текущему элементы
	previous_elements = []
	for j in range(k):
		previous_elements.append()

	ways_to_come[i] = max()


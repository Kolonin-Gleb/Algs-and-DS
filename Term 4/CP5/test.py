# ЭТОТ КОД НУЖНО ПЕРЕПИСАТЬ!
# Я НЕ ЧИСЛО СПОСОБОВ ДОЛЖЕН ОПРЕДЕЛИТЬ, А СТОИМОСТИ КАЖДОГО СПОСОБА!

import math

# ways_to_come - кол. способов прийти в те элементы, до которых можно допрыгнуть
ways_to_come = [1, 1, 1]
price_to_come = [-math.inf] * (len(ways_to_come))

count_of_prev_elements = 0
for i in range(len(ways_to_come)):
	count_of_prev_elements = i - 1

	while True: # Суммирую кол. способов добраться до пред эл.
		if i == 0:
			ways_to_come[i] = 1
			price_to_come[i] = 
			break
		else:
			ways_to_come[i] += ways_to_come[count_of_prev_elements]
			count_of_prev_elements -= 1
			if count_of_prev_elements == -1:
				break
print(ways_to_come)

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


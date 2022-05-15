# Задача - банкомат.
# Найти минимальное число банкнот, которыми можно выдать запрашиваемую сумму

import math


banknotes = [10, 60, 100] # Доступные банкноты
sum = 120 # Сумма для размена

# База (0 можно разменять 0 купюр, не получится разменять)
# Будет хранить минимальное кол. купюр, которыми можно получить сумму =
# значению индекса, в котором хранится число купюр
# ВАЖНО: Если тестируешь на маленькой сумме, то измени БАЗУ
best_exchanges = [math.inf] * (sum + 1)
best_exchanges[0] = 0
best_exchanges[10] = 1
# best_exchanges[60] = 1
# best_exchanges[100] = 1

def ATM_min_exchange(banknotes, best_exchanges, sum):
	# Если лучший исход для запрашиваемой суммы ещё не определён
	if best_exchanges[sum] == math.inf:
		for sum_for_exchange in range(1, sum + 1): # Определение суммы, которую нужно разменять
			# Сколькими купюрами возможно выдать запрашиваеммую сумму
			pos_best_exchanges = []
		
			# Рассмотрим все способы выдать запрашиваеммую сумму, начиная выдавать купюрой разного номинала
			for banknote in banknotes:
				try:
					# Попытка выдать сумму используя купюру banknote
					pos_best_exchanges.append(best_exchanges[sum_for_exchange - banknote])
				except:
					continue

			best_exchanges[sum_for_exchange] = min(pos_best_exchanges) + 1 # +1, т.к. для выдачи нужна будет ещё 1 купюра
	
	return best_exchanges[sum]

print("Минимальное число купюр, необходимое для выдачи суммы = " + str(sum) + " = ")
print(ATM_min_exchange(banknotes, best_exchanges, sum))

print(best_exchanges)


# # Задача - банкомат.
# # Найти минимальное число банкнот, которыми можно выдать запрашиваемую сумму

# import math

# banknotes = [30, 50, 100] # Доступные банкноты
# sum = 210 # Сумма для размена

# # База (0 можно разменять 0 купюр, не получится разменять)
# # Будет хранить минимальное кол. купюр, которыми можно получить сумму =
# # значению индекса, в котором хранится число купюр
# # ВАЖНО: Если тестируешь на маленькой сумме, то измени БАЗУ
# best_exchanges = [math.inf] * (sum + 1)

# # Установка базы
# best_exchanges[0] = 0
# for i in banknotes:
# 	best_exchanges[i] = 1


# def ATM_min_exchange(banknotes, best_exchanges, sum):
# 	# Если лучший исход для запрашиваемой суммы ещё не определён
# 	if best_exchanges[sum] == math.inf:
# 		for sum_for_exchange in range(1, sum + 1): # Определение суммы, которую нужно разменять
# 			# Сколькими купюрами возможно выдать запрашиваеммую сумму
# 			pos_best_exchanges = []
		
# 			# Рассмотрим все способы выдать запрашиваеммую сумму, начиная выдавать купюрой разного номинала
# 			for banknote in banknotes:
# 				try:
# 					# Попытка выдать сумму используя купюру banknote
# 					pos_best_exchanges.append(best_exchanges[sum_for_exchange - banknote])
# 				except:
# 					continue

# 			best_exchanges[sum_for_exchange] = min(pos_best_exchanges) + 1 # +1, т.к. для выдачи нужна будет ещё 1 купюра
	
# 	return best_exchanges[sum]

# def ATM_min_exchange_path(sum):
# 	ans = ATM_min_exchange(banknotes, best_exchanges, sum) # Сколько купюр нужно дать
# 	dig = sum # Какую сумму выдать
# 	path = [] # Какие купюры давать

# 	while best_exchanges[dig] != 1: # Пока от суммы не останется часть, которую можно выдать 1 купюрой
# 		for i in banknotes:
# 			if (dig - i) > 0 and best_exchanges[dig - i] == ans-1:
# 				# Если из суммы можно выдать часть = купюре И 
# 				# для оставшейся части суммы останется отдать на 1 купюру меньше
				
# 				path.append(i) # Эта купюра используется в выдаче
# 				dig = dig-i # Остаётся отдать меньше на сумму = купюре
# 				ans = ans-1 # Для выдачи остаётся на 1 купюру меньше
			
# 	path.append(dig) # Добавляем последнюю купюру
# 	return path


# min_banknotes = ATM_min_exchange(banknotes, best_exchanges, sum)
# print("Минимальное число купюр, необходимое для выдачи " + str(sum) + " = " + str(min_banknotes))

# #print("Лучшие размены для всех сумм до запрашиваемой:")
# #print(best_exchanges)

# print("Купюры, которые нужно выдать:")
# print(ATM_min_exchange_path(sum))

k = 10
for j in range(k):
	print(j)


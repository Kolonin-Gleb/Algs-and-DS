'''
Когда что использовать для решения задач:

Динамическое программирование:
1) Подзадачи повторяются (имеет смысл сохранять результаты)
2) Подзадачи немного проще задачи

Обычная рекурсия (Разделяй и властвуй):
1) Все подзадачи уникальны
2) Подзадачи значительно проще задачи (хотя бы в 2 раза)
 
'''

# числа фибоначи

import timeit

''' Разделяй и властвуй Фибоначи '''
def fib(n):
    if n < 0:
        return "error!"

    if n == 0: return 1
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)
    

# print(fib(10)) # Вывод вычисленного значения последовательности ДЛЯ ПРОВЕРКИ
# print(timeit.timeit('fib(10)', number=100, globals=globals())) # 0.01978880000000005
# print(timeit.timeit('fib(20)', number=100, globals=globals())) # 2.0884038
# print(timeit.timeit('fib(25)', number=100, globals=globals())) # 22.901690300000002

''' Динамическое решение с сохранением '''

M = {0: 0, 1: 1} # Сразу храним резултаты для первых чисел 

def fib2(n):
    if n in M:
        return M[n]
    M[n] = fib2(n - 1) + fib2(n - 2)
    return M[n]

# Тест хранения значений в словаре
# cache = {}
# cache[0] = 1

# print(cache)

# print(fib2(10)) # Вывод вычисленного значения последовательности ДЛЯ ПРОВЕРКИ
# print(timeit.timeit('fib2(10)', number=100, globals=globals())) # 0.00019780000000002573
# print(timeit.timeit('fib2(20)', number=100, globals=globals())) # 0.00011420000000006425
# print(timeit.timeit('fib2(25)', number=100, globals=globals())) # 0.00010189999999998811

''' Восходящая реализация '''
# Подсчёт всех чисел по порядку с сохранением.
# нет рекурсии есть только список, куда сохраняются значения + цикл
def fib3(n):
    nums = [0, 1]
    for i in range(2, n+1):
        nums.append(nums[i-1] + nums[i-2])
    return nums[n]

# print(fib3(10)) # Вывод вычисленного значения последовательности ДЛЯ ПРОВЕРКИ
# print(timeit.timeit('fib3(10)', number=100, globals=globals())) # 0.0008586000000000427
# print(timeit.timeit('fib3(20)', number=100, globals=globals())) # 0.0009177999999999686
# print(timeit.timeit('fib3(25)', number=100, globals=globals())) # 0.0011250000000000426



# Задача по количеству маршрутов


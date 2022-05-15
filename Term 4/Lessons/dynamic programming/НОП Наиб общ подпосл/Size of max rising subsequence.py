# Размер наибольшей возрастающей последовательности в заданном списке чисел


def largest_path(digits):
    path = [1] # База. Изначально есть как минимум 1 эл. по возростанию
    # по индексам path хранятся значения = кол. эл., которые < значения по этому же индексу в digits

    for cur in range(1, len(digits)):
        res = 0 # Сколько числел в последовательности < текущего
        for prev in range(0, cur):
            if digits[prev] < digits[cur]: # Сравнение тек. эл. с предыдущим
                if path[prev] + 1 > res:
                    res = path[prev] + 1
        path.append(res)
    return max(path)


digits = [10, 4, 13, 7, 3, 6, 17, 33]

print(largest_path(digits))


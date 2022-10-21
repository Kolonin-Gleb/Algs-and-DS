# 100 гаек и 100 болтов сортировка

from random import shuffle

# Элементы из одного списка нельзя сравнивать
screw = [i for i in range(100)]
keys = screw

shuffle(screw)
shuffle(keys)


for s in screw:
    for k in keys:
        pass

# Для формирования я буду делать словарь!


d = {
    20: ["ссылка на те, что меньше", "ссылка на те, что больше"]
}

# Быстрая сортировка. Как идея?


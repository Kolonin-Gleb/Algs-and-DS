# Задача о кузнечеке 
# Прыгать вперёд только на 2 или 3
# Число способов добраться до позиции n = число способов добраться до (n - 2) и до (n - 3)
# F(n) = F(n - 2) + F(n - 3)


# 1 0 1 - начальные позиции для расчёта остальных

def grasshopper(n):
    grasshopper=[1, 0, 1] # start positions
    for i in range(3, n+1):
        grasshopper.append(grasshopper[i-2]+ grasshopper[i-3])
    return grasshopper[n]
print(grasshopper(3))

# К.Т. по динамическому программированию на 30 баллов.


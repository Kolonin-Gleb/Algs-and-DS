#task 2.2

# Для засечения времени
import time

N = 1000
i = j = k = count = 0

start = time.time()

while i < N: #Пройти N операций здесь
    i += 1 # N операций пройдено
    while j < N: #Пройти N операций здесь
        j += 1 # 2*N операций пройдено
        while k < N: #Пройти N операций здесь
            k += 1
            count += 1 #Пройти дополнительно N операций здесь
                # 4*N операций пройдено

#4N операций, по свойству => n операций, т.к. 4 - const

#Ответ: O(n)

end = time.time()

time_spent = end - start

print("Время выполнения кода при N = " + str(N) + " будет = " + str(time_spent))



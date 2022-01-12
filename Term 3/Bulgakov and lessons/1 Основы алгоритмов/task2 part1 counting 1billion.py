#task 2.1

# Для засечения времени
import time

#Считаем до 1.000.000.000
count = 1000000000
i = 0

start = time.time()

while i <= count:
    i+=1

end = time.time()

time_spent = end - start

print("Чтобы досчитать до 1 млрд моему пк нужно = " + str(time_spent))


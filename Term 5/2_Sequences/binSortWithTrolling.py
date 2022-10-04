from math import sqrt
import math



def get_d(n):
    n = str(n)
    if '.' in n:
        return abs(n.find('.') - len(n)) - 1
    else:
        return 0


def binary_search(acc, low, high, a, c):
# Check base case
# while acc > get_d(mid):
    if high >= low:

        mid = (high + low) / 2
        if acc < high - low:
            # If element is present at the middle itself
            if mid ** a + sqrt(mid) == c:
                return mid
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif mid ** a + sqrt(mid) > c:
                return binary_search(acc, low, mid, a, c)
            # Else the element can only be present in right subarray
            else:
                return binary_search(acc, mid, high, a, c)
        else:
            return mid

    else:
        # Element is not present in the array
        return (high + low) // 2


a = int(input('Введите a: '))
c = int(input('Введите c: '))
acc = float(input('Введите точность: '))

result = binary_search(acc, a, c, a, c)

if result != -1:
	print("Приближенный ответ к", float(acc), "значениям после запятой:", str(result))
else:
	print(binary_search(acc, a, c, a, c))
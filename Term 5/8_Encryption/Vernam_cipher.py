# Отличие шифра Вермана от шифра Цезаря в том, что
# для каждого символа задаётся свой ключ (сдвиг).
# Таким образом одинаковые символы кодируются разными значениями, что круто!

from random import randint # Для получения случайного значения при формировании ключа 

# print(ord('a'), ord('z'))
# print(ord('A'), ord('Z'))

# Число ключей должно = числу букв в text
def vernam(text: str, keys = []):
    result = ""

    if keys:
        for k, letter in enumerate(text):
            if ord(letter) < 65 or ord(letter) > 90: # Для шифрования беру только большие буквы.
                result += " "
            else:
                shift = ord(letter) - int(keys[k])# - 13
                result += chr( (shift%26) + ord("A") )
        return result

    if not keys:
        for letter in text:
            key = randint(0,25)
            keys.append(key)

            if ord(letter) < 65 or ord(letter) > 90: # Для шифрования беру только большие буквы.
                result += " "
            else:
                shift = ord(letter) + key# - 13
                result += chr( (shift%26) + ord("A") ) # Результат шифрования = сдвиг в рамках алфавита + номер 1ой буквы алфавита
    
    return result, keys

# Тест шифрования
res = vernam("HELLO WORLD")
print(res)

# Тест расшифрования
res = vernam(*res)
print(res)

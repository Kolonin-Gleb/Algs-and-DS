# Вид в котором будет храниться алфавит сообщения
alphabet_eng = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def caesar(alphabet: str, text: str, step: int, mode = "encrypt"):
    # Нормализация шага
    step %= len(alphabet)

    if mode == "encrypt":
        mode = "+"
    elif mode == "decrypt":
        mode = "-"
    else:
        return "Invalid mode"

    result = ''

    for letter in text:
        position = alphabet.find(letter)
        new_position = eval(f"{position} {mode} {step}")
        new_position %= len(alphabet) # Нормализация смещения

        result += alphabet[new_position]
    return result

# Тест шифрования
res = (caesar(alphabet_eng, "HelloWorld", 4))
print(res)

# Тест расшифрования
print(caesar(alphabet_eng, res, 4, "decrypt"))


def caesar_hack(alphabet: str, text: str):
    for step in range(len(alphabet)):
        result = ''
        for letter in text:
            position = alphabet.find(letter)
            new_position = position - step
            new_position %= len(alphabet) # Нормализация смещения

            result += alphabet[new_position]
        yield result

print("===========")
print(*caesar_hack(alphabet_eng, res), sep='\n')


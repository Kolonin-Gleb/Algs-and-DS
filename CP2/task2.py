# Номер 2

# А) Необходимо использовать двухсвязный список.
# Из его середины можно будет удалять элементы по индексам не разрывая цепи.

# При добавлении каждого элемента нового цвета нужно проверить являются ли 2 предыдущие того же цвета.

# Вычислительная мощность - O(n) - линейное время

# Б)
# 1 удаление скобок. Дана строка, составленная из круглых скобок.
# Определите, какое наименьшее количество символов необходимо удалить из этой строки, чтобы
# оставшиеся символы образовывали правильную скобочную последовательность.


class Stack():
    #Constructor
    def __init__(self):
        self.stack = []

    #Методы взаимодействия со стеком
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]


# Проверить строку из 2х видов скобок на корректность

def isBracketsStringCorrect(bracketsString):
    bracketsStringLen = len(bracketsString)
    stringElement = 0
    while (stringElement < bracketsStringLen):

        if bracketsString[stringElement] == ')':
            try:
                if stack.pop() == '(':
                    stringElement += 1
                    continue
            except:
                return False
        elif bracketsString[stringElement] == ']':
            try:
                if stack.pop() == '[':
                    stringElement += 1
                    continue
            except:
                return False
        elif bracketsString[stringElement] == '(' or bracketsString[stringElement] == '[':
            stack.push(bracketsString[stringElement])
            stringElement += 1
        else:
            return False
    if stack.empty():
        return True
    else:
        return False

stack = Stack()
bracketsString = "зел зел зел красн красн желт бел"

if isBracketsStringCorrect(bracketsString) == True:
    print("Ваша строка скобок корректна!")
else:
    print("Ваша строка скобок некорректна!")


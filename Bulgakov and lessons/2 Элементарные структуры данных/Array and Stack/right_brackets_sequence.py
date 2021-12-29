#Реализация структуры данных Стек с помощью list

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
bracketsString = "([])"

if isBracketsStringCorrect(bracketsString) == True:
    print("Ваша строка скобок корректна!")
else:
    print("Ваша строка скобок некорректна!")


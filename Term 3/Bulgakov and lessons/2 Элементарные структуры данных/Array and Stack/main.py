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


# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())
# stack.pop()
# print(stack.peek())



# Развернуть строку через Стек

stack = Stack()

myString = "0123456789"

# Записал строку в стек
i = 0
while (i < len(myString)):
    stack.push(myString[i])
    print(stack.peek(), end='')
    i += 1

print('')

# Вывел строку из стека
while not (stack.empty()):
    print(stack.pop(), end='')


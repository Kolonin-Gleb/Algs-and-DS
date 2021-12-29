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


m = Stack()

m.push(1)
m.push(2)
m.push(3)

while not m.empty():
    m.pop()
    m.pop()



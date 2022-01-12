from os import system

class OneLinkNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def iterate(self):
        print("Чтение всего списка:")
        node = self.head
        while node != None:
            print(node.data)
            node = node.next
        return 0
        
    # Вернуть номер узла если нашли, иначе -1
    def find(self, searchingValue):
        index = 0
        current = self.head
        while current:
            if current.data == searchingValue:
                return index
            else:
                current = current.next
                index += 1
        return -1

    # Добавление узла с головы
    def insert(self, data):
        self.head = OneLinkNode(data, self.head)
        return 0

    # Добавление узла после 1ого узла с указанными данными.
    def insertAfter(self, data, newData):
        if self.find(data) == -1: # Если не существует узла, после которого нужно вставить новый узел
            return None
        else:
            current = self.head
            insertingNode = OneLinkNode(newData, None) # Создаем узел, что нужно будет вставить

            while current: # Пока узел существует
                if current.data == data: # Узел, после которого нужно вставить найден
                    insertingNode.next = current.next # Записываем ссылку на узел, который находится после узла, после которого будет вставлен этот узел
                    current.next = insertingNode # Вставляем новый узел после указанного
                    break
                current = current.next # Для итерации по циклу
            return 0

    # Удаление 1ого узла с данными
    def remove(self, data):
        if not self.head: # Не работаем с пустым списком
            return None
        if self.find(data) == -1: # Если не существует узла, что нужно удалить
            return None
            
        current = self.head.next

        if self.head.data == data: # Удаление головы
            del self.head
            self.head = current
            return 0

        while current.next.data != data:  # Ищем узел, после которого будет узел с необходимыми данными
            current = current.next
            
        previous = current # Создаем копию узла, после которого будет совершено удаление
        current = current.next # Дошли до удаляемого узла
        previous.next = current.next # Записываем ссылку на узел, который находится после удаляемого узла
        del current
        return 0

system("cls")

list = SinglyLinkedList()

# Не больше 9 встреч в день
# ls = ["3 Маша", "2 Саша", "5 Лена", "4 Гена"]

# sort - работает за n * log n. Можно сделать за константу!
# ls.sort(reverse=True)

# Ввод перовой задачи
print("Введите № и дело: ")
task = input()
list.insert(task)

userInput = ''
while userInput != 'exit':
    userInput = input("Введите № и дело: ")
    taskNum = userInput[0]

list.iterate()
list.remove(ls[-1])
list.iterate()

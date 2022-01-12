class BinaryTree:
    def __init__(self, rootOgj):
        self.key = rootOgj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

# Переход в правое поддерево
    def getRightChild(self):
        return self.rightChild

# Переход в левое поддерево
    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

tree = BinaryTree("A - main root")
# Создание левой ветки
tree.insertLeft("B")
tree.getLeftChild().insertLeft("D")
tree.getLeftChild().insertRight("E")
# Создание правой ветки
tree.insertRight("C")
tree.getRightChild().insertLeft("F")
tree.getRightChild().insertRight("G")

# Вывод элемента F
# print(tree.getRightChild().getLeftChild().getRootVal())

# Прямой обход дерева (сверху налево по уровням)
def preorder(tree):
    if tree: # Если узел дерева существует
        print(tree.getRootVal()) # Печать его значения
        preorder(tree.getLeftChild()) # Вызов функции для левого подузла
        preorder(tree.getRightChild())# Вызов функции для правого подузла

# preorder(tree)

# Симметричный обход дерева (сканирование слева)
def inorder(tree):
    if tree: # Если узел дерева существует
        inorder(tree.getLeftChild()) # Вызов функции для левого подузла
        print(tree.getRootVal()) # Печать его значения
        inorder(tree.getRightChild()) # Вызов функции для правого подузла

# inorder(tree)

# Обратный обход дерева (сканирование треугольниками слева)
def postorder(tree):
    if tree: # Если узел дерева существует
        postorder(tree.getLeftChild()) # Вызов функции для левого подузла
        postorder(tree.getRightChild()) # Вызов функции для правого подузла
        print(tree.getRootVal()) # Печать его значения

# postorder(tree)

# Подсчёт количества узлов в дереве
def sum_of_nodes(tree):
    if not tree:
        return 0
    return 1 + sum_of_nodes(tree.getLeftChild()) + sum_of_nodes(tree.getRightChild())


print(sum_of_nodes(tree)) # = 7


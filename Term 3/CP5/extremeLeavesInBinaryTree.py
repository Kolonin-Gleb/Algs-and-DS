import os
import random

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

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

# Прямой обход дерева (сверху налево по уровням)
def preorder(tree):
    if tree: # Если узел дерева существует
        print(tree.getRootVal()) # Печать его значения
        preorder(tree.getLeftChild()) # Вызов функции для левого подузла
        preorder(tree.getRightChild())# Вызов функции для правого подузла

# Симметричный обход дерева (сканирование слева)
def inorder(tree):
    if tree: # Если узел дерева существует
        inorder(tree.getLeftChild()) # Вызов функции для левого подузла
        print(tree.getRootVal()) # Печать его значения
        inorder(tree.getRightChild()) # Вызов функции для правого подузла

# Обратный обход дерева (сканирование треугольниками слева)
def postorder(tree):
    if tree: # Если узел дерева существует
        postorder(tree.getLeftChild()) # Вызов функции для левого подузла
        postorder(tree.getRightChild()) # Вызов функции для правого подузла
        print(tree.getRootVal()) # Печать его значения

# Вставка узла с проверкой
def insertBinary(tree, newNode):
    # Меньше идём на лево
    if newNode < tree.getRootVal():
        if not tree.getLeftChild():
            tree.insertLeft(newNode)
        else:
            insertBinary(tree.getLeftChild(), newNode)

    elif tree.getRightChild() == None:
        tree.insertRight(newNode)
    else:
        insertBinary(tree.getRightChild(), newNode)

# Подсчёт количества узлов в дереве
def get_sum_of_nodes(tree):
    if not tree:
        return 0
    return 1 + get_sum_of_nodes(tree.getLeftChild()) + get_sum_of_nodes(tree.getRightChild())

# Печать дерева по уровням.
# Вершина дерева = нулевой уровень
# Чтобы напечатать 3 уровень, нужно попасть на уровень выше
def readLevel(tree, depth):
    # Дошли до последнего листа. Дальше идти некуда
    if not tree:
        return 0 
    # Печать вершины
    if depth == 0:
        print(tree.getRootVal())
    # Печать других уровней
    elif depth > 0:
        readLevel(tree.getLeftChild(), depth-1)
        readLevel(tree.getRightChild(), depth-1)

def contain(tree, value):
    if tree: # Если узел дерева существует
        if tree.getRootVal() == value:
            return True
        else:
            preorder(tree.getLeftChild()) # Вызов функции для левого подузла
            preorder(tree.getRightChild())# Вызов функции для правого подузла

# Поиск эл. в бинарном дереве
def containBinary(tree, nodeValue):
    if not tree: # Если узел дерева существует
        return False
    else:
        if tree.getRootVal() == nodeValue:
            return True
        elif tree.getRootVal() < nodeValue:
            return containBinary(tree.getRightChild(), nodeValue)
        elif tree.getRootVal() > nodeValue:
            return containBinary(tree.getLeftChild(), nodeValue)

def getMinLeaf(tree):
    if not tree: # Если узел дерева существует
        return -1
    else:
        if tree.getLeftChild() != None:
            return getMinLeaf(tree.getLeftChild())
        else:
            return tree.getRootVal()

def getMaxLeaf(tree):
    if not tree: # Если узел дерева существует
        return -1
    else:
        if tree.getRightChild() != None:
            return getMaxLeaf(tree.getRightChild())
        else:
            return tree.getRootVal()

# Вывод кол. узлов на уровне 
def get_sum_of_nodes_on_level(tree, depth):
    # Пустое дерево
    if not tree:
        return 0
    # Только вершина
    if depth == 0:
        return 1
    # Много узлов на уровне
    elif depth > 0:
        return get_sum_of_nodes_on_level(tree.getLeftChild(), depth-1) + get_sum_of_nodes_on_level(tree.getRightChild(), depth-1)

# Если у узла нет детей, то это лист
def get_sum_of_leaves(tree):
    if tree:
        if tree.getLeftChild() == None and tree.getRightChild() == None:
            return 1
        else:
            return get_sum_of_leaves(tree.getLeftChild()) + get_sum_of_leaves(tree.getRightChild())
    else:
        return 0

def get_depth(tree):
    if not tree:
        return 0
    else:
        left_depth = get_depth(tree.getLeftChild())
        right_depth = get_depth(tree.getRightChild())

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1



os.system('cls')

nums = [8, 3, 1, 10, 11, 13, 6, 4, 7]

#random.shuffle(nums)
print(nums)

# Заполнение дерева
treeHead = nums.pop(0) # Забор 1 элемента для головы

tree = BinaryTree(treeHead)

for i in nums:
    insertBinary(tree, i)

print("Вывод дерева")
inorder(tree)


# В бинарном дереве минимальный лист лежит слева, а максимальный справа

print("Минимальный лист")
print(getMinLeaf(tree))

print("Максимальный лист")
print(getMaxLeaf(tree))


#строим бинарное дерево
#создаёт список из корневого узла и 2 пустых подсписков

def BinaryTree(r):
    return [r, [], []]

def setRootVal(root, newVal):
    root[0] = newVal

def getRootVal(root):
    return root[0]

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


#имеющегося левого спускаем на уровень ниже
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch, t, []])
    else:
        root.insert(1,[newBranch, [], []])
    return root

#имеющегося правого спускаем на уровень ниже
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch, t, []])
    else:
        root.insert(2,[newBranch, [], []])
    return root

r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print(l)

setRootVal(l, 9)
print(r)

insertLeft(l, 11)
print(r)

print(getRightChild(getRightChild(r)))


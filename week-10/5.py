class TreeNode():
    def __init__ (self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = [0, 9, 4, 2, 8, 1]

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)

findName = 9
current = root
while True:
    if findName == current.data:
        print(findName, "을(를) 찾음.")
        break
    elif findName < current.data:
        if current.left == None:
            print(findName, '이(가) 트리에 없음.')
            break
        current = current.left
    else:
        if current.right == None:
            print(findName, "이(가) 트리에 없음.")
            break
        current = current.right
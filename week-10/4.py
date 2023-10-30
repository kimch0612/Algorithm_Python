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

def preorder(node):
    if node == None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

print("이진 탐색 트리 구성 완료!")
preorder(root)
print("끝!")
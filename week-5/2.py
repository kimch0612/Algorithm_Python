class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insertData
    current.link = node

memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

if __name__ == "__main__":
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data_ in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data_
        pre.Link = node
        memory.append(node)
    
    printNodes(head)

    insertNode("다현", "화사")
    printNodes(head)
    insertNode("사나", "솔라")
    printNodes(head)
    insertNode("재남", "문별")
    printNodes(head)
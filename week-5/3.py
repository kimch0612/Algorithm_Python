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

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

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

    deleteNode("다현")
    printNodes("head")
    deleteNode("쯔위")
    printNodes("head")
    deleteNode("지효")
    printNodes("head")
    deleteNode("재남")
    printNodes("head")
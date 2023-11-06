class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(nameAry[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(nameAry[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end=' ')
        print()
    print()

def findVertex(g, findVtx):
    stack = []
    visitedAry = []
    current = 0
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(gSize):
            if g.graph[current][vertex] != 0:
                if vertex in visitedAry:
                    pass
                else:
                    next = vertex
                    break
            if next != None:
                current = next
                stack.append(current)
                visitedAry.append(current)
            else:
                current = stack.pop()
    if findVtx in visitedAry:
        return True
    else:
        return False


def isQueueEmpty():
    global SIZE, queue, front, rear
    if (rear == front): return True
    else: return False

# def enQueue(data):
#     global SIZE, queue, front, rear
#     if (isQueueFull()):
#         print("큐가 가득 찼습니다.")
#         return
#     rear += 1
#     queue[rear] = data

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

print("큐가 비어있는지 여부 -> ", isQueueEmpty())
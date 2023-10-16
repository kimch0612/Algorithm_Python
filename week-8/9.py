def isQueueFull():
    global SIZE, queue, front, rear
    if rear != SIZE - 1: return False
    elif (rear == SIZE - 1) and (front == -1): return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

SIZE = 5
queue = [None, None, "3", "4", "5"]
front = 1
rear = 4

print("queue가 꽉 찼나? --> ", isQueueFull())
print("큐 상태 --> ", queue)
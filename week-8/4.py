def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE): return True
    else: return False

SIZE = 5
queue = ["1", "2", "3", "4", "5"]
front = -1
rear = len(queue)

print("queue가 꽉 찼나? --> ", isQueueFull())
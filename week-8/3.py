def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE - 1): return True
    else: return False

SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

rear += 1
queue[rear] = "화사"
rear += 1
queue[rear] = "솔라"
rear += 1
queue[rear] = "문별"

print("---- 큐 상태 ----")
print("[출구] <--", end=' ')
for i in range(0, len(queue)): print(queue[i], end=' ')
print("<-- [입구]")

for i in range(3):
    front += 1
    data = queue[front]
    queue[front] = None
    print('deQueue --> ', data)

print("---- 큐 상태 ----")
print("[출구] <-- ", end = ' ')
for i in range(0, len(queue), 1): print(queue[i], end=' ')
print("<-- [입구]")
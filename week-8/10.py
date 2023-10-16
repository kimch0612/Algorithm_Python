def enQueue(data):
    global SIZE, queue, front, rear
    # if (isQueueFull()):
    #     print("큐가 가득 찼습니다.")
    #     return
    rear += 1
    queue[rear] = data

queue = [None, None, "3", "4", "5"]
rear = -1

print(queue)
enQueue("가나다")
print(queue)
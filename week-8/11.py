def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1) % SIZE == front): return True
    else: return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear): return True
    else: return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 가득 찼습니다.")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    return queue[(front+1) % SIZE]

SIZE = int(input("큐 크기를 입력하세요 -> "))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":
    select = input("I E V X --> ")

    while (select != 'X' and select != 'x'):
        if select == 'I':
            data = input("입력할 데이터 --> ")
            enQueue(data)
            print("큐 상태: ", queue)
            print("front: ", front, ", rear: ", rear)
        elif select == "E":
            data = deQueue()
            print("추출된 데이터 --> ", data)
            print("큐 상태: ", queue)
            print("front: ", front, ", rear: ", rear)
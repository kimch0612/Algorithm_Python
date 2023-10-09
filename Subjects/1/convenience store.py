import random
import math

# Node 클래스 정의
class Node():
    def __init__(self):
        self.data = None  # 노드에 저장될 데이터
        self.link = None  # 다음 노드를 가리키는 링크(포인터)

# 편의점 정보를 출력하는 함수
def printStores(start):
    current = start  # 현재 노드를 가리키는 포인터
    if current is None:  # 만약 시작 노드가 없으면 함수 종료
        return
    
    while current.link != head:  # 현재 노드가 시작 노드(head)를 가리키지 않는 동안 반복
        current = current.link  # 다음 노드로 이동
        x, y = current.data[1:]
        # 편의점 이름과 해당 편의점까지의 거리를 계산하여 출력
        print(current.data[0], '편의점 거리: ', math.sqrt(x*x + y*y))
    print()

# 편의점 리스트를 생성하는 함수
def makeStoreList(store):
    global memory, head, current, pre

    node = Node()  # 새로운 노드 생성
    node.data = store  # 노드에 편의점 정보 저장
    memory.append(node)  # 생성한 노드를 메모리에 추가

    if head is None:  # 시작 노드가 없다면 현재 노드를 시작 노드로 설정
        head = node
        node.link = head
        return
    
    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX * nodeX + nodeY * nodeY)  # 새로운 편의점까지의 거리 계산
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX * headX + headY * headY)  # 시작 노드까지의 거리 계산

    if headDist > nodeDist:  # 시작 노드까지의 거리가 새로운 편의점까지의 거리보다 크다면
        node.link = head  # 새로운 노드를 시작 노드로 만들고, 기존의 연결 유지
        last = head
        while last.link != head:  # 연결 리스트의 끝까지 이동
            last = last.link
        last.link = node
        head = node  # 새로운 노드를 시작 노드로 설정
        return
    
    current = head
    while current.link != head:  # 현재 노드가 시작 노드를 가리키지 않는 동안 반복
        pre = current  # 이전 노드를 저장
        current = current.link  # 다음 노드로 이동
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX * currX + currY * currY)  # 현재 노드까지의 거리 계산
        if currDist > nodeDist:  # 현재 노드까지의 거리가 새로운 편의점까지의 거리보다 크다면
            pre.link = node  # 이전 노드의 링크를 새로운 노드로 변경
            node.link = current  # 새로운 노드의 링크를 현재 노드로 변경
            return
    
    current.link = node  # 연결 리스트의 끝에 새로운 노드 추가
    node.link = head  # 새로운 노드를 시작 노드로 설정

memory = []  # 노드 메모리
head, current, pre = None, None, None  # 시작 노드와 현재 노드, 이전 노드 초기화

if __name__ == "__main__":
    storeArray = []  # 편의점 정보를 저장할 리스트
    storeName = 'A'
    for _ in range(10):
        store = (storeName, random.randint(1, 100), random.randint(1, 100))
        storeArray.append(store)
        storeName = chr(ord(storeName) + 1)
    
    for store in storeArray:
        makeStoreList(store)  # 편의점 정보를 연결 리스트에 추가
    
    printStores(head)  # 편의점 정보 출력

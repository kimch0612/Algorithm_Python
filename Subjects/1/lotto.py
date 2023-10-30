#컴퓨터소프트웨어학과 2학년 20102056 김창환
import random # 난수를 생성하기 위한 모듈.

class Node(): # Linked List 역할을 맡을 Node 클래스를 정의.
    def __init__(self):
        self.data = None
        self.link = None

def printLotto(start): # 로또 번호를 출력하는 함수를 정의.
    current = start
    if current is None: return # 만약 연결 리스트가 비어있다면 아무것도 출력하지 않는다.
    print(current.data, end=' ') # 첫 번째 노드의 데이터를 출력.
    while current.link != None:
        current = current.link
        print(current.data, end=' ') # 다음 노드의 데이터를 출력.
    print()

def addLottoNum(num): # 로또 번호를 Linked List에 추가하는 함수를 정의.
    global memory, head, current, pre
    node = Node() # 새로운 노드를 생성.
    node.data = num # 노드에 로또 번호를 저장.
    memory.append(node) # memory 리스트에 노드를 추가.
    if head is None:
        head = node # 만약 연결 리스트가 비어있다면, 새로운 노드를 head로 지정.
        return
    if head.data > num:
        node.link = head
        head = node # 새로운 노드를 head로 지정하고, 기존의 head와 연결.
        return
    current = head
    while current.link != head and current.link != None:
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current # 새로운 노드를 적절한 위치에 삽입.
            return
    current.link = node

def isthisviable(num): # 지정한 번호가 이미 연결 리스트에 있는지 확인하는 함수를 정의.
    global memory, head, current, pre
    if head is None: return False # 연결 리스트가 비어있다면 해당 번호가 없으므로 False를 반환.
    current = head
    if current.data is num: return True # 첫 번째 노드의 데이터가 찾고자 하는 번호와 일치하면 True를 반환.
    while current.link != None:
        current = current.link
        if current.data is num: return True # 다음 노드의 데이터가 찾고자 하는 번호와 일치하면 True를 반환.
    return False # 연결 리스트를 모두 검사했지만 해당 번호를 찾지 못하면 False를 반환.

memory = [] # 노드 메모리를 관리하기 위한 리스트.
head, current, pre = None, None, None # Linked List의 시작 노드, 현재 노드, 이전 노드
 
if __name__ == '__main__':
    lottoCount = 0
    while True:
        lotto = random.randint(1, 45) # 1부터 45까지의 난수를 생성하여 로또 번호로 사용.
        if isthisviable(lotto): continue # 이미 생성한 번호인 경우, 다시 생성.
        lottoCount += 1
        addLottoNum(lotto) # 새로운 로또 번호를 연결 리스트에 추가.
        if lottoCount >= 6: break # 6개의 로또 번호가 생성됐다면 종료.
    printLotto(head) # 생성한 로또 번호를 출력.
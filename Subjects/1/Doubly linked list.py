class Node2():
    def __init__(self):
        self.plink = None  # 이전 노드에 대한 링크
        self.data = None   # 노드의 데이터
        self.nlink = None  # 다음 노드에 대한 링크

def printNodes(start):
    current = start
    if current.nlink is None:
        return
    print("정방향 --> ", end=' ')
    print(current.data, end=' ')
    while current.nlink is not None:
        current = current.nlink
        print(current.data, end=' ')
    print()
    print("역방향 --> ", end=' ')
    print(current.data, end=' ')
    while current.plink is not None:
        current = current.plink
        print(current.data, end=' ')
    print()
    
memory = []            # 노드 객체들을 저장하는 리스트
head, current, pre = None, None, None  # 연결 리스트 관련 변수 초기화
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]  # 데이터 배열

if __name__ == "__main__":
    node = Node2()
    node.data = dataArray[0]
    head = node  # 헤드 노드 설정
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node  # 이전 노드의 다음 노드로 현재 노드 연결
        node.plink = pre  # 현재 노드의 이전 노드로 이전 노드 연결
        memory.append(node)  # 노드를 메모리 리스트에 추가
    
    printNodes(head)  # 연결 리스트 출력

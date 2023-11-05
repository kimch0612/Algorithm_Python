'''
컴퓨터소프트웨어학과 2학년 20102056 김창환
파이썬 알고리즘 2nd 과제: 이진탐색트리 구현
목표: 검색, 삽입, 삭제 함수 구현
이때, 삭제는 0, 1, 2인 경우에도 모두 포함
'''

# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.root = None    # 노드의 부모 (사용하지 않음)
        self.left = None    # 왼쪽 자식 노드
        self.right = None   # 오른쪽 자식 노드
        self.data = data    # 현재 노드의 데이터 값

# 이진 탐색 트리 클래스 정의, Node 클래스를 상속
class BinarySearchTree(Node):
    def insert(self, data):
        # 새로운 데이터를 삽입하는 함수
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        # 재귀 함수로 삽입을 처리하는 함수
        if node is None:
            node = Node(data)  # 새로운 노드 생성
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)  # 왼쪽 서브트리에 삽입
            else:
                node.right = self._insert_value(node.right, data)  # 오른쪽 서브트리에 삽입
        return node

    def find(self, key):
        # 주어진 키 값을 찾는 함수
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        # 재귀 함수로 키 값을 찾는 함수
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)  # 왼쪽 서브트리에서 검색
        else:
            return self._find_value(root.right, key)  # 오른쪽 서브트리에서 검색

    def delete(self, key):
        # 주어진 키 값을 삭제하는 함수
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        # 재귀 함수로 삭제를 처리하는 함수
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # 삭제할 노드가 두 개의 자식을 가질 때
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                # 삭제할 노드가 하나의 자식을 가질 때
                node = node.left or node.right
            else:
                # 삭제할 노드가 자식이 없을 때
                node = None
        elif key < node.data:
            # 왼쪽 서브트리에서 삭제를 시도
            node.left, deleted = self._delete_value(node.left, key)
        else:
            # 오른쪽 서브트리에서 삭제를 시도
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

# 이진 탐색 트리 객체 생성
bst = BinarySearchTree(None)

# 데이터 리스트 정의
data_list = [50, 1, 0, 20, 40, 60, 2]

# 데이터 리스트의 값들을 이진 탐색 트리에 삽입
for data in data_list:
    bst.insert(data)

# 검색할 키 정의
search_key = 40

# 키를 찾았는지 여부 확인
if bst.find(search_key):
    print(f"{search_key}을(를) 찾았습니다.")
else:
    print(f"{search_key}을(를) 찾지 못했습니다.")

# 삭제할 키 정의
delete_key = 0

# 키를 삭제했는지 여부 확인
if bst.delete(delete_key):
    print(f"{delete_key}을(를) 삭제했습니다.")
else:
    print(f"{delete_key}을(를) 삭제하지 못했습니다.")

# 다른 키에 대해서도 삭제를 시도
delete_key = 1
if bst.delete(delete_key):
    print(f"{delete_key}을(를) 삭제했습니다.")
else:
    print(f"{delete_key}을(를) 삭제하지 못했습니다.")
delete_key = 2
if bst.delete(delete_key):
    print(f"{delete_key}을(를) 삭제했습니다.")
else:
    print(f"{delete_key}을(를) 삭제하지 못했습니다.")

# 삭제 후, 해당 키가 여전히 존재하는지 여부 확인
if bst.find(0):
    print(f"{0}을(를) 찾았습니다.")
else:
    print(f"{0}을(를) 찾지 못했습니다.")
if bst.find(1):
    print(f"{1}을(를) 찾았습니다.")
else:
    print(f"{1}을(를) 찾지 못했습니다.")
if bst.find(2):
    print(f"{2}을(를) 찾았습니다.")
else:
    print(f"{2}을(를) 찾지 못했습니다.")

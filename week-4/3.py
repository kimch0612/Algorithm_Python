friends = ['다현', '정연', '쯔위', '사나', '지효']

def del_data(location):

    size = len(friends)
    if location < 0 or location > size:
        print("데이터가 범위를 벗어났습니다.")
        return
    friends[location] = None
    for _ in range(location + 1, size):
        friends[_ - 1] = friends[_]
        friends[_] = None
    del(friends[size-1])

del_data(1)
print(friends)
del_data(3)
print(friends)
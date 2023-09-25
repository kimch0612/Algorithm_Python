friends = ['다현', '정연', '쯔위', '사나', '지효']

def insert_value(location, name):
    if location < 0 or location > len(friends):
        print("범위를 벗어났습니다.")
        return
    
    friends.append(None)
    size = len(friends)

    for _ in range(size - 1, location, -1):
        friends[_] = friends[_ - 1]
        friends[_ - 1] = None
    
    friends[location] = name

insert_value(2, '솔라')
print(friends)
insert_value(6, '문별')
print(friends)
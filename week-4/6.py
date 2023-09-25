def find_insert_data(friend, k_count):
    findPos = -1
    for _ in range(len(katok)):
        pair = katok[_]
        if k_count >= pair[1]:
            findPos = _
            break
    if findPos == -1:
        findPos = len(katok)

    insert_data(findPos, (friend, k_count))

def insert_data(location, friend):
    if location < 0 or location > len(katok):
        print("범위를 벗어났습니다.")
        return
    katok.append(None)
    size = len(katok)
    for _ in range(size - 1, location, -1):
        katok[_] = katok[_ - 1]
        katok[_ - 1] = None
    
    katok[location] = friend

katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
data = input("추가할 친구 --> ")
count = int(input("카톡 횟수 ---> "))
find_insert_data(data, count)
print(katok)
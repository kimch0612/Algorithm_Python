friends = ['다현', '정연', '쯔위', '사나', '지효']

def del_data(location):
    if location < 0 or location > len(friends):
        print("데이터가 범위를 벗어났습니다.")
        return
    while True:
        try: del(friends[location])
        except: break
    return friends

print(del_data(2))
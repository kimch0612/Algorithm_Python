friends = []

def move_data(friend):
    friends.append(None)
    fri_size = len(friends)
    friends[fri_size - 1] = friend

move_data('다현')
move_data('정연')
move_data('쯔위')
move_data('사나')
move_data('지효')

print(friends)
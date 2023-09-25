list1 = []
list2 = []
i = 0
value = 12
num = 0
for _ in range(0, 4):
    for __ in range(0, 3):
        list1.append(value)
        value -= 1
    list2.append(list1)
    list1 = []

for i in range(0, 4):
    for __ in range(0, 3):
        print("%3d" % list2[i][__], end="")
        num += list2[i][__]
    print(" ")
print("배열의 합: %d" % num)
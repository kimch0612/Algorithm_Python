aa = []
a = 0
for _ in range(0, 5): aa.append(input(str(_ + 1) + "번째 숫자: "))
for _ in range(0, len(aa)): a += int(aa[_])
print(aa)
print(a)
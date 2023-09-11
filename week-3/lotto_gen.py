import random
allLotto = []

print("//// 로또번호 자동 생성을 시작합니다 ////")
for _ in range(int(input("생성할 횟수를 입력하세요: "))):
    lotto = []
    while True:
        rnd = random.randint(1, 45)
        if rnd not in lotto: lotto.append(rnd)
        if len(lotto) >= 6: break
    allLotto.append(lotto)
for lotto_list in allLotto:
    lotto_list.sort()
    print("자동번호---> ", end=' ')
    for _ in range(0, 6): print("%2d" % lotto_list[_], end=' ')
    print()
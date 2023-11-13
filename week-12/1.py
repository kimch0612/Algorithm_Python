def calNum(a, b):
    if a >= b: return a
    else: return a + calNum(a+1, b)
a, b = map(int, input("숫자 1과 2를 차례대로 입력하세요: ").split())
if a > b: a, b = b, a
print(calNum(a, b))
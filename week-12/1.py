def calNum(a, b):
    if a >= b: return a
    else: return a + calNum(a+1, b)

a = int(input("숫자1 ---> "))
b = int(input("숫자2 ---> "))
print(calNum(a, b))
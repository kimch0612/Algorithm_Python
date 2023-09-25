def multi(num1, num2):
    mulList = []
    res = num1 + num2
    res2 = num1 - num2
    mulList.append(res)
    mulList.append(res2)
    return mulList

myList = []
add, sub = 0, 0

myList = multi(3, 1)
add = myList[0]
sub = myList[1]
print("%d %d" % (add, sub))
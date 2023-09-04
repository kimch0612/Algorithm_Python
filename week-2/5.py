def multi(num1, num2):
    mulList = []
    mulList.append(num1 + num2), mulList.append(num1 - num2), mulList.append(num1 * num2), mulList.append(int(num1 / num2)), mulList.append(num1 % num2), mulList.append(num1 ** num2)
    return mulList

myList = multi(100, 20)
print(myList)
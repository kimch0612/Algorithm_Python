def multi(num1, num2):
    mulList = []
    mulList.append(num1 + num2), mulList.append(num1 - num2), mulList.append(num1 * num2), mulList.append(int(num1 / num2)), mulList.append(num1 % num2), mulList.append(num1 ** num2)
    return mulList

print(multi(100, 20))
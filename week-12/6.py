def palindrome(pStr):
    if len(pStr) <= 1: return True
    if pStr[0] != pStr[-1]: return False
    return palindrome(pStr[1:len(pStr)-1])

strAry = ["reaver", "kayak", "abba", "hello", "asdfdsa"]

for testStr in strAry:
    print(testStr, end='---> ')
    testStr = testStr.lower().replace(' ', '')
    if palindrome(testStr): print('O')
    else: print('X')
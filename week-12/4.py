def gugu(dan, num):
    print("%d x %d = %d  " % (dan, num, dan*num), end=' ')
    if dan < 9: gugu(dan+1, num)
for num in range(1, 10):
    gugu(2, num)
    print()
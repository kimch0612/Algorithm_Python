num = int(input("구구단?: "))
for _ in range(1, 10):
    print("%d * %d = %d" % (num, _, num*_))
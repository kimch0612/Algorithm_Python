def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):
        for cur in range(end, 0, -1):
            if (ary[cur-1] > ary[cur]):
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary
dataAry = [162, 786, 444, 555, 9542, 44532, 1]

print("정렬 전 --> ", dataAry)
dataAry = insertionSort(dataAry)
print("정렬 후 --> ", dataAry)
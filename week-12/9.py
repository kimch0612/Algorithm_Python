def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]): minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
    
    return ary

dataAry = [100, 162, 21, 75, 1000, 455, 999]

print("진행 전 --> ", dataAry)
dataAry = selectionSort(dataAry)
print("진행 후 --> ", dataAry)
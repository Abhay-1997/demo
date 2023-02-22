processArray = [50, 5, 6, 72, -1]
for i in processArray:
    if i > 49 and i % 6 == 0:
        print(-2)
    elif i == 5:
        print(5)
    elif i > 49:
        print(-1)
    elif i % 6 == 0:
        print(-5)


processArray = [3, 6, 36, 61, 121, 66, 26, 376, 661, 6, -1]
n = processArray. copy()
for i in range(len(processArray)):
    if processArray[i] < 0:
        n.remove(processArray[i])
    elif processArray[i] % 2 != 0:
        continue

    else:
        if processArray[i] % 2 == 0 and processArray[i+1] % 2 == 0:
            n.remove(processArray[i+1])
for i in n:
    print(i)

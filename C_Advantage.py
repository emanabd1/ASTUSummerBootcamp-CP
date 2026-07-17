t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    temp = arr[:]
    temp.sort()

    mx = temp[-1]
    sec = temp[-2]

    res = []

    for num in arr:
        if num == mx:
            res.append(num - sec)
        else:
            res.append(num - mx)

    print(*res)
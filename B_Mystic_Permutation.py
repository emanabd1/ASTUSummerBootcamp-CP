t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    b = sorted(a)

    for i in range(n - 1):
        if b[i] == a[i]:
            b[i], b[i + 1] = b[i + 1], b[i]

    if b[-1] == a[-1]:
        b[-1], b[-2] = b[-2], b[-1]

    print(*b)
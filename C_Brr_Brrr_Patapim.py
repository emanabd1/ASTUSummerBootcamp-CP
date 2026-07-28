t = int(input())

for _ in range(t):
    n = int(input())

    p = [0] * (2 * n + 1)
    used = [False] * (2 * n + 1)

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if i == 0:
                p[j + 2] = row[j]
            elif j == n - 1:
                p[i + n + 1] = row[j]
            used[row[j]] = True

    for x in range(1, 2 * n + 1):
        if not used[x]:
            p[1] = x
            break

    print(*p[1:])
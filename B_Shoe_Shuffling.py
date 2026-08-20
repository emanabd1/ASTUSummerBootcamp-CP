t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    ans = list(range(1, n + 1))

    i = 0
    possible = True

    while i < n:
        j = i

        # Find the group of equal shoe sizes
        while j < n and s[j] == s[i]:
            j += 1

        # Group has only one person
        if j - i == 1:
            possible = False
            break

        # Right rotation
        ans[i] = j

        for k in range(i + 1, j):
            ans[k] = k

        i = j

    if possible:
        print(*ans)
    else:
        print(-1)
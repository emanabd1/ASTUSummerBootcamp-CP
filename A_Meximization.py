from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)

    ans = []

    for x in sorted(cnt):
        ans.append(x)
        cnt[x] -= 1

    for x in sorted(cnt):
        ans.extend([x] * cnt[x])

    print(*ans)
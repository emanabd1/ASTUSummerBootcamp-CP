t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    ans = [-1] * n
    seen = set()
    removed = 0

    for time, post in enumerate(p, 1):
        if post not in seen:
            seen.add(post)
            removed += 1
            idx = n - removed
            if idx >= 0:
                ans[idx] = time

    print(*ans)
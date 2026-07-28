t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))

    prefix = [0]

    for x in arr:
        prefix.append(prefix[-1] + x)

    total = prefix[-1]

    for _ in range(q):
        l, r, k = map(int, input().split())

        old = prefix[r] - prefix[l - 1]
        new = total - old + (r - l + 1) * k

        print("YES" if new % 2 else "NO")
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    cnt = 0
    ok = True

    for ch in s:
        if ch == '1':
            cnt += 1
            if cnt >= k:
                ok = False
                break
        else:
            cnt = 0

    if not ok:
        print("NO")
        continue

    print("YES")

    ans = [0] * n
    lo = 1
    hi = n

    
    for i in range(n):
        if s[i] == '0':
            ans[i] = hi
            hi -= 1

    
    for i in range(n):
        if s[i] == '1':
            ans[i] = lo
            lo += 1

    print(*ans)

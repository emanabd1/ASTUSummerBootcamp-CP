t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    limit = a[0] - 1
    print(*[min(x, limit) for x in queries])
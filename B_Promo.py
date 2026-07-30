n, q = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

prefix = [0]
for x in a:
    prefix.append(prefix[-1] + x)

for _ in range(q):
    x, y = map(int, input().split())
    print(prefix[x] - prefix[x - y])
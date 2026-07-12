t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    left_min = [0] * n
    right_min = [0] * n

    left_min[0] = 0
    for i in range(1, n):
        if p[i] < p[left_min[i - 1]]:
            left_min[i] = i
        else:
            left_min[i] = left_min[i - 1]

    right_min[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if p[i] < p[right_min[i + 1]]:
            right_min[i] = i
        else:
            right_min[i] = right_min[i + 1]

    found = False

    for j in range(1, n - 1):
        i = left_min[j - 1]
        k = right_min[j + 1]

        if p[i] < p[j] and p[k] < p[j]:
            print("YES")
            print(i + 1, j + 1, k + 1)
            found = True
            break

    if not found:
        print("NO")
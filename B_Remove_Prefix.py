t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    used = set()
    answer = 0

    index = n - 1
    while index >= 0:
        if arr[index] in used:
            answer = index + 1
            break

        used.add(arr[index])
        index -= 1

    print(answer)
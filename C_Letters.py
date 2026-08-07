n, m = map(int, input().split())

a = list(map(int, input().split()))
q = list(map(int, input().split()))

prefix = []
total = 0

for x in a:
    total += x
    prefix.append(total)

for x in q:
    
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2

        if prefix[mid] >= x:
            right = mid
        else:
            left = mid + 1

    dorm = left

    if dorm == 0:
        room = x
    else:
        room = x - prefix[dorm - 1]

    print(dorm + 1, room)

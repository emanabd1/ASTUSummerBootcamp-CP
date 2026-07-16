n = int(input())
s = input()

rooms = [0] * 10

for c in s:
    if c == 'L':
        for i in range(10):
            if rooms[i] == 0:
                rooms[i] = 1
                break
    elif c == 'R':
        for i in range(9, -1, -1):
            if rooms[i] == 0:
                rooms[i] = 1
                break
    else:
        rooms[int(c)] = 0

print("".join(map(str, rooms)))
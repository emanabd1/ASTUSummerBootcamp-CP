t = int(input())

for _ in range(t):
    n = int(input())

    first = input().split()
    second = input().split()
    third = input().split()

    count = {}

    for word in first:
        count[word] = count.get(word, 0) + 1

    for word in second:
        count[word] = count.get(word, 0) + 1

    for word in third:
        count[word] = count.get(word, 0) + 1

    score1 = 0
    score2 = 0
    score3 = 0

    for word in first:
        if count[word] == 1:
            score1 += 3
        elif count[word] == 2:
            score1 += 1

    for word in second:
        if count[word] == 1:
            score2 += 3
        elif count[word] == 2:
            score2 += 1

    for word in third:
        if count[word] == 1:
            score3 += 3
        elif count[word] == 2:
            score3 += 1

    print(score1, score2, score3)
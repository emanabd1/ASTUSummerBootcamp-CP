t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    solved = set()
    balloons = 0

    for problem in s:
        if problem in solved:
            balloons += 1
        else:
            balloons += 2
            solved.add(problem)

    print(balloons)
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()

    smallest = nums[0]
    second_smallest = nums[1]
    second_largest = nums[-2]
    largest = nums[-1]

    answer = largest + second_largest - smallest - second_smallest

    print(answer)
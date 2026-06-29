t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    unique_elements = len(set(a))
    
    if unique_elements <= (n // 2) + 1:
        print("YES")
    else:
        print("NO")
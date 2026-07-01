t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    possible = True
    for i in range(n):
        
        pos = i + 1 
        
        min_dist = min(pos, n - pos + 1)
        
        if p[i] < min_dist:
            possible = False
            break
            
    if possible:
        print("YES")
    else:
        print("NO")
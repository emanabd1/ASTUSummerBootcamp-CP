t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pref1 = [0] * (n + 1)

    
    pref2 = [0] * (n + 1)

    for i in range(n):
        if a[i] == 1:
            pref1[i + 1] = pref1[i] + 1
            pref2[i + 1] = pref2[i] + 1
        elif a[i] == 2:
            pref1[i + 1] = pref1[i] - 1
            pref2[i + 1] = pref2[i] + 1
        else:
            pref1[i + 1] = pref1[i] - 1
            pref2[i + 1] = pref2[i] - 1

    possible = False

  

    min_pref2 = float('inf')

    for j in range(2, n):
        i = j - 1

       
        if pref1[i] >= 0:
            min_pref2 = min(min_pref2, pref2[i])

        
        if pref2[j] >= min_pref2:
            possible = True
            break

    print("YES" if possible else "NO")
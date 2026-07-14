import sys

def solve():
    
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    
    a = [0] + [int(x) for x in data[2:n+2]]
    
    
    pref = [0] * (n + 1)
    for i in range(2, n + 1):
        damage = max(0, a[i-1] - a[i])
        pref[i] = pref[i-1] + damage
        
     
    suff = [0] * (n + 2)
    for i in range(n - 1, 0, -1):
        damage = max(0, a[i+1] - a[i])
        suff[i] = suff[i+1] + damage

    
    idx = n + 2
    output = []
    for _ in range(m):
        s = int(data[idx])
        t = int(data[idx+1])
        idx += 2
        
        if s < t:
            
            output.append(str(pref[t] - pref[s]))
        else:
            
            output.append(str(suff[t] - suff[s]))
            

    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()

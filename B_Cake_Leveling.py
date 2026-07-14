import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        
        
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        current_sum = 0
        ans = float('inf')
        res = []
        
        for i in range(n):
            current_sum += a[i]
            max_h_at_i = current_sum // (i + 1)
            
            
            if max_h_at_i < ans:
                ans = max_h_at_i
                
            res.append(str(ans))
            
        out.append(" ".join(res))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()

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
        p = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        

        safe_count_from = [0] * (n + 2)
        total_safe = 0
        
        for i in range(n, 0, -1):
            p_i = p[i-1]
            is_safe = 1 if p_i <= i else 0
            safe_count_from[i] = safe_count_from[i+1] + is_safe
            if is_safe:
                total_safe += 1
        
        
        max_chairs = total_safe
        
       
        for k in range(1, n + 1):
            p_k = p[k-1]
            if p_k > k:
                
                unreachable_safe = safe_count_from[p_k]
                current_score = total_safe - unreachable_safe + 1
                
                if current_score > max_chairs:
                    max_chairs = current_score
                    
        out.append(str(max_chairs))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
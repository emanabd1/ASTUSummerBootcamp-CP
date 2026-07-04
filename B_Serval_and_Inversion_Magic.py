import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        
        blocks = 0
        in_mismatch = False
        
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                if not in_mismatch:
                    blocks += 1
                    in_mismatch = True
            else:
                in_mismatch = False
                
        if blocks <= 1:
            out.append("Yes")
        else:
            out.append("No")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
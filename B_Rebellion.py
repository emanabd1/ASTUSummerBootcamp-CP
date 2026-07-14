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
        
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        left = 0
        right = n - 1
        operations = 0
        
        while left < right:
            
            while left < right and a[left] == 0:
                left += 1
             
            while left < right and a[right] == 1:
                right -= 1
                
            
            if left < right:
                operations += 1
                left += 1
                right -= 1
                
        out.append(str(operations))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

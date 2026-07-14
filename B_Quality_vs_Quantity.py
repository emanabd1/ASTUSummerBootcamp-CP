import sys

def solve():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        a = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
         
        a.sort()
        
        left = 1
        right = n - 1
        
        sum_blue = a[0]
        sum_red = 0
        
        possible = False
        
        
        while left < right:
            sum_blue += a[left]
            sum_red += a[right]
            
            if sum_red > sum_blue:
                possible = True
                break
                
            left += 1
            right -= 1
            
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()

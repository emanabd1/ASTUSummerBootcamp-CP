import sys

def solve():
    # Read all input from standard input efficiently
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
        
        # 1. Sort the array
        a.sort()
        
        # 2. Initialize pointers and initial sums
        # Blue starts with the single smallest element
        left = 1
        right = n - 1
        
        sum_blue = a[0]
        sum_red = 0
        
        possible = False
        
        # 3. Process pairs greedily
        while left < right:
            sum_blue += a[left]
            sum_red += a[right]
            
            # At this exact point: Count(Blue) == Count(Red) + 1
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
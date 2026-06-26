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
        s = input_data[idx + 1]
        idx += 2
        target = s[-1]
        saved_characters = s.count(target)
        ans = n - saved_characters
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
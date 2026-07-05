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
        m = int(input_data[idx+1])
        k = int(input_data[idx+2])
        
        # Convert strings to sorted lists of characters
        a = sorted(list(input_data[idx+3]))
        b = sorted(list(input_data[idx+4]))
        idx += 5
        
        c = []
        i, j = 0, 0
        consec_a = 0
        consec_b = 0
        
        # Loop until either string 'a' or 'b' runs out of characters
        while i < n and j < m:
            # Condition 1: We must pick from 'b' because 'a' hit the limit k
            if consec_a == k:
                c.append(b[j])
                j += 1
                consec_b = 1
                consec_a = 0
            # Condition 2: We must pick from 'a' because 'b' hit the limit k
            elif consec_b == k:
                c.append(a[i])
                i += 1
                consec_a = 1
                consec_b = 0
            # Condition 3: Neither hit the limit, pick the smaller character
            else:
                if a[i] < b[j]:
                    c.append(a[i])
                    i += 1
                    consec_a += 1
                    consec_b = 0
                else:
                    c.append(b[j])
                    j += 1
                    consec_b += 1
                    consec_a = 0
                    
        out.append("".join(c))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
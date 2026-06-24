


import sys


tokens = sys.stdin.read().split()
if tokens:
    t = int(tokens[0])
    idx = 1
    for _ in range(t):
        n = int(tokens[idx])
        
        a = tokens[idx + 1 : idx + 1 + n]
        print("Yes" if "100" in a else "No")
        idx += 1 + n
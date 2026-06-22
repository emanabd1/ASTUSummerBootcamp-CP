import sys

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        a = [int(x) for x in input_data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        out.append(str((max(a) - min(a) + 1) // 2))
    sys.stdout.write('\n'.join(out) + '\n')
import sys


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    out_lines = []
    idx = 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        s = data[idx]; idx += 1
        # count differing adjacent pairs in circular string
        D = 0
        for i in range(n):
            if s[i] != s[(i + 1) % n]:
                D += 1
        # maximum blocks is min(n, D+1)
        ans = D + 1
        if ans > n:
            ans = n
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()


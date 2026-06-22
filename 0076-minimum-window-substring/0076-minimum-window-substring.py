class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = Counter(t), Counter()
        req, have_cnt, l, res = len(need), 0, 0, (float('inf'), 0, 0)
        
        for r, char in enumerate(s):
            have[char] += 1
            if char in need and have[char] == need[char]:
                have_cnt += 1
            while have_cnt == req:
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_cnt -= 1
                l += 1
        return s[res[1]:res[2]+1] if res[0] != float('inf') else ""
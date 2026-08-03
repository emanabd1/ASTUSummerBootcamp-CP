class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)

        chars = [c for c in freq if freq[c] >= k]
        chars.sort(reverse=True)

        limit = {c: freq[c] // k for c in chars}
        used = Counter()

        ans = ""

        def check(word):
            target = word * k
            j = 0

            for c in s:
                if j < len(target) and c == target[j]:
                    j += 1

            return j == len(target)

        def dfs(word):
            nonlocal ans

            if len(word) > len(ans):
                ans = word

            for c in chars:
                if used[c] == limit[c]:
                    continue

                used[c] += 1
                candidate = word + c

                if check(candidate):
                    dfs(candidate)

                used[c] -= 1

        dfs("")
        return ans
        
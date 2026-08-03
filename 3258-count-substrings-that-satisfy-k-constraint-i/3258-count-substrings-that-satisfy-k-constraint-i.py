class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        left = 0
        ans = 0
        zeros = 0
        ones = 0

        for right in range(len(s)):
            if s[right] == '0':
                zeros += 1
            else:
                ones += 1

            while zeros > k and ones > k:
                if s[left] == '0':
                    zeros -= 1
                else:
                    ones -= 1
                left += 1

            ans += right - left + 1

        return ans
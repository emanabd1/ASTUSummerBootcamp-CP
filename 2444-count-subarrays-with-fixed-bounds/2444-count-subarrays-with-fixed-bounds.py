class Solution:
    def countSubarrays(self, nums, minK, maxK):
        ans = 0

        last_min = -1
        last_max = -1
        last_invalid = -1

        for i, x in enumerate(nums):
            if x < minK or x > maxK:
                last_invalid = i

            if x == minK:
                last_min = i

            if x == maxK:
                last_max = i
            ans += max(0, min(last_min, last_max) - last_invalid)

        return ans
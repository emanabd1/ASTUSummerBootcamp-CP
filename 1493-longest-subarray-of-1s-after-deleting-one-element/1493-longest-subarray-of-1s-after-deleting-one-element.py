class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = l = zeros = 0
        for r in range(len(nums)):
            zeros += nums[r] == 0
            while zeros > 1:
                zeros -= nums[l] == 0
                l += 1
            max_len = max(max_len, r - l)
        return max_len
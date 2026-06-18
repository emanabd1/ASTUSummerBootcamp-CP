class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[0:k])
        max_sum = window_sum
        
        for i in range(k, n):
            left = i - k
            right = i
            window_sum = window_sum - nums[left] + nums[right]
            max_sum = max(window_sum, max_sum)
            
        return max_sum / k
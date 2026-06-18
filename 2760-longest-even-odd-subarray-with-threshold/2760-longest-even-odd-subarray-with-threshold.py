class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        l = -1 
        
        for r in range(len(nums)):
            if nums[r] > threshold:
                l = -1
                continue
            
            if l == -1:
                if nums[r] % 2 == 0:
                    l = r
            else:
                if nums[r] % 2 == nums[r - 1] % 2:
                    if nums[r] % 2 == 0:
                        l = r
                    else:
                        l = -1
            
            if l != -1:
                max_len = max(max_len, r - l + 1)
                
        return max_len
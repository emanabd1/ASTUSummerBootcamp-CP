class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        min_heap = []
        max_val = float('-inf')
        
        for i, row in enumerate(nums):
            heapq.heappush(min_heap, (row[0], i, 0))
            max_val = max(max_val, row[0])
            
        min_val, _ = min_heap[0][0], min_heap[0][1]
        ans = [min_val, max_val]
        
        while len(min_heap) == len(nums):
            val, r, c = heapq.heappop(min_heap)
            
            if max_val - val < ans[1] - ans[0]:
                ans = [val, max_val]
            elif max_val - val == ans[1] - ans[0] and val < ans[0]:
                ans = [val, max_val]
                
            if c + 1 < len(nums[r]):
                next_val = nums[r][c + 1]
                heapq.heappush(min_heap, (next_val, r, c + 1))
                max_val = max(max_val, next_val)
            else:
                break
                
        return ans
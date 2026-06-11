class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        total_count = 0
        target_str = str(digit)
        
        for num in nums:
            num_as_str = str(num)
            appearances = num_as_str.count(target_str)
            total_count = total_count + appearances
            
        return total_count
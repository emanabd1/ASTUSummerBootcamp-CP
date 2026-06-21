class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = streak = 1
        for i in range(1, len(prices)):
            streak = streak + 1 if prices[i] == prices[i - 1] - 1 else 1
            total += streak
        return total
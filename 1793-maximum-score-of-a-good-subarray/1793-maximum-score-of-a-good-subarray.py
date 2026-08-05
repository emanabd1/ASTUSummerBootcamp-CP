class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        left = right = k
        minimum = nums[k]
        answer = minimum

        while left > 0 or right < n - 1:
            if left == 0:
                right += 1
            elif right == n - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1

            minimum = min(minimum, nums[left], nums[right])
            answer = max(answer, minimum * (right - left + 1))

        return answer


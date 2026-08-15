class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                result = max(result, current_count)
            else:
                current_count = 0
        return result
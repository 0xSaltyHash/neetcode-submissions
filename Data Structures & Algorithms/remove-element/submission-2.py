class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0
        length = len(nums)
        while pointer < length:
            if nums[pointer] == val:
                length -= 1
                nums[pointer] = nums[length]
            else:
                pointer += 1
        return pointer

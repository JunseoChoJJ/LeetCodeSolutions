class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        newList = sorted(nums)

        return nums.index(newList[-1])

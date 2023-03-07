class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        
        if len(nums) == 0:
            return cnt
        
        for i in range(len(nums)):
            if i+1 == len(nums):
                break

            if nums[i+1] <= nums[i]:
                cnt += nums[i] - nums[i+1] + 1
                nums[i+1] = nums[i] + 1
        
        print(nums)
        return cnt

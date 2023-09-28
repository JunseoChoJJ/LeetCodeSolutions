'''
I use dat method (direct address table) I think concepts are right however I got memory limit exceeded
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        print(max(nums))
        dat = [0] * (max(nums) + 1)
        nums = sorted(nums)
        tmp = nums[0]
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != tmp:
                dat[tmp] = cnt
                cnt = 1
                tmp = nums[i]
            else:
                cnt += 1
        dat[tmp] = cnt
        print(dat)
        return dat.index(max(dat))
'''
# In the description it says it.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

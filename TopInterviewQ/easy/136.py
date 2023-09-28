class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        nums = sorted(nums)
        mode = nums[0]
        curr_cnt = 1
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if mode == nums[i]:
                curr_cnt += 1
            else:
                if curr_cnt == 1:
                    return mode
                else:
                    mode = nums[i]
                    curr_cnt = 1
        
        return mode

'''
class Solution(object):
    def singleNumber(self, nums):
        # Initialize the unique number...
        uniqNum = 0;
        # TRaverse all elements through the loop...
        for idx in nums:
            # Concept of XOR...
            uniqNum ^= idx;
        return uniqNum;   



'''

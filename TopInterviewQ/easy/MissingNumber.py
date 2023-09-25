class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums) + 1):
            if nums.count(i) == 0:
                return i
        

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return ((n*(n+1))//2)-(sum(nums))

use math 
'''

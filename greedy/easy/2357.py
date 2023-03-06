class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        expectation = [0] * len(nums)
        
        while True:
            if nums == expectation:
                break
            x = min(i for i in nums if i != 0)
            for j in range(len(nums)):
                if nums[j] != 0:
                    nums[j] -= x
            cnt += 1
         
        return cnt

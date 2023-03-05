class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(len(nums))
        sum = 0
        for i in range(0,len(nums),2):
            print(nums[i])
            sum += nums[i]
            #print(sum)

        return sum
        '''
        best solution
        return sum(sorted(nums)[::2])
        '''

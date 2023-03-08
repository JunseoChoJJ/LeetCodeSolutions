class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        print(nums)
        print(len(nums))
        nums.sort(reverse = True)
        
        for i in range(len(nums)):
            if i == len(nums) - 2:
                break

            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
                break
        
        return 0

    
        '''

        why nums = nums.sort(reverse = True)

        gives me just the count number?

        '''

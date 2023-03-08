class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        num = num[::-1]
        print(num)
        
        
        for i in range(len(num)):
            
            if int(num[i]) % 2 != 0:
                ans += num[i:]
                break
        
        print(ans)
        return ans[::-1]

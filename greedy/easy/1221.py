class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        result = 0
        cnt = 0
        for i in s:
            if i == "R":
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                result += 1

        return result

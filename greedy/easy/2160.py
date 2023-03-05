class Solution:
    def minimumSum(self, num: int) -> int:
        x = list(str(num))
        x.sort()
        
        
        firstNum = x[0] + x[2]
        secondNum = x[1] + x[3]
        firstNum = int(firstNum)
        secondNum = int(secondNum)

        return firstNum + secondNum

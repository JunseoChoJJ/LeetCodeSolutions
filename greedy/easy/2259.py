class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        #gameplan: you just need to find out first appearance digit remove and the last 
        
        result = 0

        for i in range(len(number)):
            if number[i] == digit:
                result = max(result, int(number[0:i] + number[i+1:len(number)]))
        return str(result)
    

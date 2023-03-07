class Solution:
    def maximum69Number (self, num: int) -> int:

        # gameplan : 
        num = list(str(num))
        
        for i in range(len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        print(num)
    
        return int(''.join(num))

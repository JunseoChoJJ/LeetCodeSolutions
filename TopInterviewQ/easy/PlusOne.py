class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""

        for i in range(len(digits)):
            if digits[i] != "0":
                length = i
                break
            
            
        for digit in digits[length:]:
            num += str(digit)
        print(num)


        num2 = int(num) + 1


        ans = []

        for num in str(num2):
            ans.append(int(num))

        print(ans)
        return ans

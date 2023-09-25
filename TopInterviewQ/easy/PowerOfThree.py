class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            while True:
                if n == 1:
                    break
                if n % 3 != 0:
                    return False
                n = n // 3
            return True

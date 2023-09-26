class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()

'''
other method using not above format

s[:] = s[::-1]
'''

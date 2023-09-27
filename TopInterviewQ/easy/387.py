class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = set(s)

        for i in range(len(s)):
            hi = 0
            for j in range(len(s)):
                if s[i] == s[j] and i != j:
                    hi += 1
                    break
            if hi == 0:
                return i
        return -1

  '''
  I used for loop twice. so I need to find more time complexity less.
  use enumerate method to count
  class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,c in enumerate(s):
            print(c)
            if s.count(c)==1:
                return i
                
        return -1
  '''

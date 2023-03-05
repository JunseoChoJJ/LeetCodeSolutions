class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = list(s)
        t = set(s)
        print(t)
        if len(t) == 1 and len(s) >= 2:
            return len(s)

        ans = []
        for i in t:
            n = s.count(i)
            ans.append(n)
        
        print(ans)
        count = 0
        x = 0
        for j in ans:
            if j > 1:
                if j % 2 == 0:
                    x += 1
                    count += j
                else:
                    count += j - 1
            
        if x == len(ans):
            return count
        return count + 1
        
        '''
        
        

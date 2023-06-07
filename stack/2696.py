class Solution:
    def minLength(self, s: str) -> int:
        
        one = "AB"
        two = "CD"
        stack = []

        stack = []
        for c in s:
            stack.append(c)
            if stack:
                if ''.join(stack[-2:]) == one:
                    stack.pop()
                    stack.pop()
                elif ''.join(stack[-2:]) == two:
                    stack.pop()
                    stack.pop()
        print(stack)
        return len(stack)

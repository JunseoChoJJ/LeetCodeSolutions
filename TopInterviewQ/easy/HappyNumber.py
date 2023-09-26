class Solution:
    def isHappy(self, n: int) -> bool:

        print(n)

        total = 0
        tmp = n
        
        for num in str(tmp):
            total += int(num) * int(num)
        tmp = total
        total = 0
        for num in str(tmp):
            total += int(num) * int(num)
        tmp = total
    
        while True:
            if len(str(tmp)) == 1:
                if tmp == 1:
                    return True
                else:
                    return False
            else:
                total = 0
                for num in str(tmp):
                    total += int(num) * int(num)
                tmp = total



'''
I think my answer is hard coding so I need to look up the solutions.
class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n != 1:
            if n in hset: return False
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True

'''

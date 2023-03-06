class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        cnt = 0

        current = current.split(":")
        correct = correct.split(":")

        possible = [15, 5, 1]
        
        hour = int(correct[0]) - int(current[0])
        
        cnt += hour
        
        minute = int(correct[1]) - int(current[1])
        if minute < 0:
            cnt -= 1
            minute = 60 - abs(minute) 

        print(minute)
        for i in possible:
            cnt += minute // i
            minute = minute % i
            

        return cnt

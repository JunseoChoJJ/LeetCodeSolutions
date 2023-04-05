class Solution:
    def minMaxDifference(self, num: int) -> int:

        num = str(num)

        mapNum = ""
        minNum = num[0]
        for i in num:
            if i != "9":
                mapNum += i
                break

        maxAns = ""
        minAns = ""

        for i in range(len(num)):
            if num[i] == mapNum:
                maxAns += "9"
            else:
                maxAns += num[i]
        for j in range(len(num)):
            if num[j] == minNum:
                minAns += "0"
            else:
                minAns += num[j]
        print(maxAns)
        print(minAns)
        print(int(minAns))

        

        return int(maxAns) - int(minAns)

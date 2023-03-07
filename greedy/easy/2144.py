class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        #gameplan: iterate through reverse and put it in 
        if len(cost) <= 2:
            return sum(cost)
        cost.sort(reverse=True)
        
        print(cost)
        ans = []
        j = 2
        for i in range(len(cost)):

            if i == j: 
                j += 3
                continue
            else:
                ans.append(cost[i])
        print(ans)
        return sum(ans)

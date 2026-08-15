class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_costs = [0,0]
        for i in range(2, len(cost)+1):
            min_costs.append(min(cost[i-1] + min_costs[i-1], cost[i-2]+min_costs[i-2]))
        
        return min_costs[-1]
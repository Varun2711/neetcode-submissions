class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1, 2]
        if n <= 2:
            return table[n-1]

        for i in range(2, n+1):
            table.append(table[i-1] + table[i-2])
        
        return table[n-1]
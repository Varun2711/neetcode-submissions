class Solution:
    def climbStairs(self, n: int) -> int:
        rf = 5**(1/2)

        return round((((1+rf)/2)**(n+1) - ((1-rf)/2)**(n+1))/rf)
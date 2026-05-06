class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                sidx, stemp = stack.pop()
                res[sidx] = i - sidx
            stack.append((i, temp))
        return res                    



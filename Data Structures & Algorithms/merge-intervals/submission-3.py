class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        stack = []

        for interval in intervals:
            start, end = interval
            if stack and stack[-1][1] >= start:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append(interval)

        return stack
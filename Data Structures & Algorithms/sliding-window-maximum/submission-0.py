class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        if len(nums) < k:
            return [max(nums)]

        q = collections.deque()

        res = []

        i = 0
        while i < k:
            q.append(nums[i])
            i += 1
        res.append(max(q))
        while i < len(nums):
            q.popleft()
            q.append(nums[i])
            res.append(max(q))
            i+= 1

        
        return res

        


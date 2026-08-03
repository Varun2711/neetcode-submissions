class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 1
        res = []

        for n in nums:
            res.append(x)
            x *= n

        x = 1
        for i in range(len(nums)-1, -1, -1):
            res[i]*= x
            x*= nums[i]

        return res
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i, n in enumerate(nums):

            if n > 0:
                break

            if i > 0 and n == nums[i-1]:
                continue

            
            l, r = i + 1, len(nums)-1

            while l < r:
                x = nums[l] + nums[r] + n

                if x > 0:
                    r -= 1
                
                elif x < 0:
                    l += 1

                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
                    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, k in enumerate(nums):
            if target-k in num_map:
                return [num_map[target-k], i]
            num_map[k] = i
            

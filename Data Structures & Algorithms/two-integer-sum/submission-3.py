class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, v in enumerate(nums):
            if (target - v) in num_map:
                return [num_map[target-v], i]
            
            num_map[v] = i
        
        return [-1, -1]
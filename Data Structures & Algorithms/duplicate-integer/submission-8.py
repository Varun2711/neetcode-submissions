class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqs = {}

        for n in nums:
            freqs[n] = 1 + freqs.get(n, 0)
            if (freqs[n] > 1):
                return True
        
        return False


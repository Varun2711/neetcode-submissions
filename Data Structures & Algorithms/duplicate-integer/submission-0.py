class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_so_far = list()

        for num in nums:
            if num in nums_so_far:
                return True
            else:
                nums_so_far.append(num)

        return False
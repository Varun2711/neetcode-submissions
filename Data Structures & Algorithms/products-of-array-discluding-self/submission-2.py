class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        for i in nums:
            prefixes.append(prefixes[-1]*i)

        suffixes = [1]
        for i in nums[::-1]:
            suffixes.append(suffixes[-1]*i)

        prefixes.pop()
        suffixes.pop()

        res = []
        for i, j in zip(prefixes, suffixes[::-1]):
            res.append(i*j)

        return res

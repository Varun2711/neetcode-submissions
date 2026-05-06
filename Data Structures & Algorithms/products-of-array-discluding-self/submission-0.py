class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1];

        for n in nums:
            prefix_products.append(prefix_products[-1]*n)


        suffix_products = [1]
        for n in nums[::-1]:
            suffix_products.append(n*suffix_products[-1])

        prefix_products.pop()
        suffix_products.pop()

        res = []
        for i, j in zip(prefix_products, suffix_products[::-1]):
            res.append(i*j)
        return res
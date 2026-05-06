class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height)-1
        max_l = 0
        max_r = len(height)-1

        while l < r:
            if height[max_l] < height[max_r]:
                l += 1
                if height[max_l] < height[l]:
                    max_l = l
                else:
                    total += height[max_l] - height[l]
            else:
                r -= 1
                if height[max_r] < height[r]:
                    max_r = r
                else:
                    total += height[max_r] - height[r]
        
        return total
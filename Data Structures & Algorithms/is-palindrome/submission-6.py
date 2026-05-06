class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = ''.join([char for char in s.lower() if char.isalnum()])
        
        l, r = 0, len(s_lower) - 1

        while l < r:
            x = s_lower[l]
            y = s_lower[r]

            if not x == y and x.isalnum() and y.isalnum():
                return False
            else:
                l += 1
                r -= 1


        return True
            
            

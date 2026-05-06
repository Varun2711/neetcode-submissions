class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        y = ''
        for char in x:
            if char.isalnum():
                y = y + char

        return y == y[::-1]
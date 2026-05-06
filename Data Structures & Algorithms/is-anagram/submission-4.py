
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCounts = [0]*26

        for char in s:
            charCounts[ord(char) - ord('a')] += 1
        
        for char in t:
            charCounts[ord(char)-ord('a')] -= 1
        
        return all(i == 0 for i in charCounts)
        
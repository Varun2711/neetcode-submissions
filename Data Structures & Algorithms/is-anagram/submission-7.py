class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = [0] * 26
        t_counts = [0] * 26

        for c in s:
            s_counts[ord(c)-97] += 1
        
        for c in t:
            t_counts[ord(c) - 97] += 1

    
        return s_counts == t_counts
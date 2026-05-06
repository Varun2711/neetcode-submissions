class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = sorted(s1)
        for i in range(0, len(s2)-len(s1)+1):
            if sorted(s2[i:i+len(s1)]) == a:
                return True
        return False

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            x = ''.join(sorted(s))
            if x in anagrams:
                anagrams[x].append(s)
            else:
                anagrams[x] = [s]
        
        return list(anagrams.values())

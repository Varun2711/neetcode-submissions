class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:

            key = tuple(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return groups.values()

        


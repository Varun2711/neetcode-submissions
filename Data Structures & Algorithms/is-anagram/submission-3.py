
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = dict()

        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        print(char_map)
        for char in t:
            if not char in char_map:
                return False
            else:
                char_map[char] -= 1
                
        return all(i == 0 for i in char_map.values())
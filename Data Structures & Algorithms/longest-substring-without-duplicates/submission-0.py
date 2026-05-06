class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = collections.deque()
        longest = 0
        for char in s:
            while char in queue:
                queue.popleft()
            queue.append(char)
            longest = max(longest, len(queue))
        return longest

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l = 0
        maxf = 0
        longest = 0

        for r in range(len(s)):
            window[s[r]] += 1
            maxf = max(maxf, window[s[r]])

            while (r-l+1) - maxf > k:
                window[s[l]] -= 1
                l += 1
            longest = max(longest, r -l + 1)
        return longest
                
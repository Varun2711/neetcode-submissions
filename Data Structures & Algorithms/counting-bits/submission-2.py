class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]
        for num in range(1, n+1):
            if num & 1:
                counts.append(1 + counts[num >> 1])
            else:
                counts.append(counts[num >> 1])

        return counts
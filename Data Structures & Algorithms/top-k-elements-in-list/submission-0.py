import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            if n in counts:
                counts[n]+=1
            else:
                counts[n] = 1

        elements = counts.keys()
        c = counts.values()

        res = [e for e, x in sorted(zip(elements, c), key=operator.itemgetter(1))][-k:]
        return res


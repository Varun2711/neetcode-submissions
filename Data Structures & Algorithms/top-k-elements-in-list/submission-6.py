from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = [[] for i in range(len(nums) + 1)]
        counts = defaultdict(int)
        for num in nums: 
            counts[num] += 1

        for num, cnt in counts.items():
            freq_list[cnt].append(num)

        res = []
        for i in range(len(freq_list) -1, 0, -1):
            for num in freq_list[i]:
                res.append(num)
                if len(res) == k:
                    return res


        

        

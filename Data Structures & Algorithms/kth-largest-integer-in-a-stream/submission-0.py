import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -1*val)

        items = []
        for i in range(self.k-1):
            items.append(heapq.heappop(self.nums))
        
        x = -1 * self.nums[0]

        for i in items:
            heapq.heappush(self.nums, i)

        return x
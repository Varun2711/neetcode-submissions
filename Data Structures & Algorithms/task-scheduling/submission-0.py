class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        max_heap = []
        q = collections.deque()
        time = 0

        for count in counts.values():
            heapq.heappush(max_heap, -count)

        while max_heap or q:
            time += 1

            if max_heap:
                x = 1+ heapq.heappop(max_heap)
                if x:
                    q.append([x, time + n])

            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time


        
        
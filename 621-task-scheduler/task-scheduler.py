class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        while max_heap:
            temp = []

            for _ in range(n+1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))

            for count in temp:
                if count + 1 < 0:
                    heapq.heappush(max_heap, count + 1)
            
            time += (n + 1) if max_heap else len(temp)
        
        return time
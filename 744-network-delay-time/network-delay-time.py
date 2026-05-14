class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v,w))

        pq = [(0,k)]

        distances = [float('inf')]*(n+1)
        distances[k] = 0

        while pq:
            currentDist, currentNode = heapq.heappop(pq)

            if currentDist > distances[currentNode]:
                continue

            for nextNode, weight in graph[currentNode]:
                nextDist = currentDist + weight

                if nextDist < distances[nextNode]:
                    distances[nextNode] = nextDist
                    
                    heapq.heappush(pq, (nextDist, nextNode))
        maxDist = max(distances[1:])

        return -1 if maxDist == float('inf') else maxDist
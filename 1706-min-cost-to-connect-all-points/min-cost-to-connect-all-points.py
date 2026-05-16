class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        pq = [(0,0)]

        in_mst = [False] * n
        min_cost = 0
        points_connected = 0

        while points_connected < n:
            distance, current = heapq.heappop(pq)

            if in_mst[current]:
                continue

            in_mst[current] = True
            min_cost += distance
            points_connected += 1

            for i in range(n):
                if not in_mst[i]:
                    dist = (
                        abs(points[current][0] - points[i][0]) +
                        abs(points[current][1] - points[i][1])
                    )

                    heapq.heappush(pq, (dist, i))

        return min_cost
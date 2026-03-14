class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        prov = 0

        for i in range(n):
            if not visited[i]:
                self.bfs(isConnected, visited, i)
                prov += 1

        return prov
    
    def bfs(self, isConnected, visited, start):
        q = deque([start])
        visited[start] = True

        while q:
            city = q.popleft()

            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)
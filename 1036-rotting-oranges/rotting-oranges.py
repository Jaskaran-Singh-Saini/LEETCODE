class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        fresh_count = 0
        rotten_queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j))

        if fresh_count == 0:
            return 0
        
        direc = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0

        while rotten_queue:
            size = len(rotten_queue)

            for _ in range(size):
                x,y = rotten_queue.popleft()

                for dx, dy in direc:
                    nx, ny = x+dx, y+dy

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        rotten_queue.append((nx,ny))
            minutes += 1
        
        return minutes - 1 if fresh_count == 0 else -1
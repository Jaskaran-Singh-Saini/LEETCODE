class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n= len(grid)

        l = grid[0][0]
        r = n*n-1

        while l < r:
            mid = l + (r - l) // 2

            if self.canSwim(grid,mid):
                r = mid
            else:
                l = mid + 1
        return l

    def canSwim(self, grid, t):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        return self.dfs(grid, visited, 0, 0, t)

    def dfs(self, grid, visited, i, j, t):
        n = len(grid)

        if (
            i<0 or i>=n or
            j<0 or j>=n or
            visited[i][j] or
            grid[i][j] > t
        ):
            return False
        
        if i== n-1 and j== n-1:
            return True
        
        visited[i][j] = True                    

        return (
            self.dfs(grid, visited, i+1, j, t) or
            self.dfs(grid, visited, i-1, j, t) or
            self.dfs(grid, visited, i, j+1, t) or
            self.dfs(grid, visited, i, j-1, t)
        )
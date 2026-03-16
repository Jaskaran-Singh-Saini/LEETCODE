class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j)
                    max_area = max(max_area, area)

        return max_area


    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0

        grid[i][j] = 0   # mark visited
        area = 1

        area += self.dfs(grid, i + 1, j)
        area += self.dfs(grid, i - 1, j)
        area += self.dfs(grid, i, j + 1)
        area += self.dfs(grid, i, j - 1)

        return area
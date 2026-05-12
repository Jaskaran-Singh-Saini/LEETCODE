class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        row = len(heights)
        col = len(heights[0])

        pr = [[False] * col for i in range(row)]
        ar = [[False] * col for i in range(row)]

        def dfs(r, c, reach):
            direc = [(0,1), (1,0), (-1,0), (0,-1)]

            reach[r][c] = True

            for dr, dc in direc:
                newRow= r + dr
                newCol = c + dc

                if(
                    newRow < 0 or newRow >= row or
                    newCol < 0 or newCol >= col
                ):
                    continue

                if reach[newRow][newCol]:
                    continue
                
                if heights[newRow][newCol] < heights[r][c]:
                    continue
                
                dfs(newRow, newCol, reach)

        for i in range(row):
            dfs(i, 0, pr)
        
        for j in range(col):
            dfs(0, j , pr)

        for i in range(row):
            dfs(i, col-1, ar)

        for j in range(col):
            dfs(row-1, j, ar)

        res = []

        for i in range(row):
            for j in range(col):
                if pr[i][j] and ar[i][j]:
                    res.append([i, j])
        
        return res
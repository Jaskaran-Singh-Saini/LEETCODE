class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(i,j):
            if i < 0 or i >= m or j>=n or board[i][j] != 'O':
                return
            
            board[i][j] = 'T'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(m):
            for j in range(n):
                if (i==0 or i ==m-1 or j==0 or j==n-1) and board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
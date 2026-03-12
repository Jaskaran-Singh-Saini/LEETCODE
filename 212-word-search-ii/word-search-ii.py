class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.result = []

        root = TrieNode()
        for word in words:
            node = root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.word = word
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in root.children:
                    self.backtracking(row, col, root)
        
        return self.result

    def backtracking(self, row, col, parent):
        letter = self.board[row][col]
        currNode = parent.children[letter]

        if currNode.word is not None:
            self.result.append(currNode.word)
            currNode.word = None

        self.board[row][col] = '#'

        rowOffset = [-1,0,1,0]
        colOffset = [0,1,0,-1]

        for i in range(4):
            newRow = row + rowOffset[i]
            newCol = col + colOffset[i]

            if(
                newRow < 0
                or newCol < 0
                or newRow >= len(self.board)
                or newCol >= len(self.board[0])
            ):
                continue

            if self.board[newRow][newCol] in currNode.children:
                self.backtracking(newRow, newCol, currNode)

        self.board[row][col] = letter

        if not currNode.children:
            parent.children.pop(letter)
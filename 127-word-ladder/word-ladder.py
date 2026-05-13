class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)

        allComboDict = {}

        for word in wordList:
            for i in range(L):
                newWord = word[:i] + "*" + word[i+1:]

                transform = allComboDict.get(newWord, [])
                transform.append(word)
                allComboDict[newWord] = transform

        Q = deque()
        Q.append((beginWord, 1))

        visited = {}
        visited[beginWord] = True

        while Q:
            word, level = Q.popleft()

            for i in range(L):

                newWord = word[:i] + '*' + word[i+1:]

                for adjacentWord in  allComboDict.get(newWord, []):
                    if adjacentWord == endWord:
                        return level + 1

                    if adjacentWord not in visited:
                        visited[adjacentWord] = True
                        Q.append((adjacentWord, level + 1))

        return 0
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]

        node.word = True
    
    def searchInNode(self, word, node):
        for i in range(len(word)):
            ch = word[i]

            if ch not in node.children:
                if ch == '.':
                    for child in node.children.values():
                        if self.searchInNode(word[i+1:], child):
                            return True
                return False
            else:
                node = node.children[ch]
        
        return node.word

    def search(self, word: str) -> bool:
        return self.searchInNode(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
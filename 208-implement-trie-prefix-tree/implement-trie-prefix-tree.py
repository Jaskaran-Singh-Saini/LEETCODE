class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False

    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node

    def setEnd(self):
        self.isEnd = True
    
    def is_end(self):
        return self.isEnd

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def searchPrefix(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find (node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        for u, v in edges:
            root1 = find(u)
            root2 = find(v)
            if root1 == root2:
                return [u, v]
            
            parent[root2] = root1
        
        return []
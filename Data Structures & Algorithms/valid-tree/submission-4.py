from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 

        graph = {i: [] for i in range(n)}

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src) 

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False

            return True
        return dfs(0, -1) and len(visited) == n
                
                    

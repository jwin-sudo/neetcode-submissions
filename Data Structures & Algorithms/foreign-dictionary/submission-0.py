from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char : set() for word in words for char in word}
        indegree = {char : 0 for char in adj}

        for i in range(0, len(words) - 1, 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    before = word1[j]
                    after = word2[j]

                    if after not in adj[before]:
                        adj[before].add(after)
                        indegree[after] += 1
                    
                    break 
            
        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in adj[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(adj):
            return ""
            
        return "".join(result)
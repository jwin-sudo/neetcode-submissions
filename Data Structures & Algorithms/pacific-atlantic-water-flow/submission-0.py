from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS = len(heights)
        COLUMNS = len(heights[0])

        def bfs(start):
            seen = set(start)
            queue = deque(start)

            while queue:
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c

                    if (0 <= nr < ROWS) and (0 <= nc < COLUMNS) and heights[nr][nc] >= heights[r][c] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))

            return seen 

        pacific_start = [(r, 0) for r in range(ROWS)] + [(0, c) for c in range(COLUMNS)]
        atlantic_start = [(ROWS-1, c) for c in range(COLUMNS)] + [(r, COLUMNS-1) for r in range(ROWS)]

        pacific_reachable = bfs(pacific_start)
        atlantic_reachable = bfs(atlantic_start)

        return [(r,c) for (r,c) in pacific_reachable & atlantic_reachable]






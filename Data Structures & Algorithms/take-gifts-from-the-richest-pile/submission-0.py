import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for _ in range(k):
            current_max = max(gifts)
            current_index = gifts.index(current_max)

            gifts[current_index] = math.floor(math.sqrt(gifts[current_index]))
        
        return sum(gifts)
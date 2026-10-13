class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach_so_far = 0
        
        for i in range(len(nums)):
            if i > reach_so_far:
                return False 
                
            reach_so_far = max(reach_so_far, i+nums[i])

            if reach_so_far >= len(nums) - 1:
                return True
        return False 
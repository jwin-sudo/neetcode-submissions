class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        n = len(nums)

        curr_total = 0 
        for i in range(n):
            curr_total += nums[i]

            max_so_far = max(curr_total, max_so_far)

            if curr_total < 0:
                curr_total = 0 
                continue
        return max_so_far
            

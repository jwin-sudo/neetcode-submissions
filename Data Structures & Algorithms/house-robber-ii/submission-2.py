class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob1 = 0
        rob2 = 0 

        for i in range(0, len(nums)-1):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2 
            rob2 = temp 
        
        first_pass = rob2 

        rob3 = 0 
        rob4 = 0 
        for j in range(1, len(nums), 1):
            temp = max(nums[j] + rob3, rob4)
            rob3 = rob4 
            rob4 = temp 
        
        second_pass = rob4

        return max(first_pass, second_pass)
            
            
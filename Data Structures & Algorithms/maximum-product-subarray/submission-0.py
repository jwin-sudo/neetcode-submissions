class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [0] * len(nums)
        max_dp[0] = nums[0]

        min_dp = [0] * len(nums)
        min_dp[0] = nums[0]

        result = nums[0]

        for i in range(1, len(nums), 1):
            num = nums[i]

            max_dp[i] = max(
                num, 
                max_dp[i-1] * num,
                min_dp[i-1] * num
            )

            min_dp[i] = min(
                num,
                max_dp[i-1] * num,
                min_dp[i-1] * num
            )

            result = max(result, max_dp[i])
        
        return result

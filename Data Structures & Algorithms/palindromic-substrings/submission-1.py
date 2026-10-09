class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [False] * n

        count = 0

        for i in range(n-1, -1, -1):
            for j in range(n-1, i - 1, -1):

                dp[j] = (
                    s[i] == s[j]
                    and (j-i <= 2 or dp[j-1])
                )

                if dp[j]:
                    count += 1
        return count 
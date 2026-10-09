class Solution:
    def numDecodings(self, s: str) -> int:
        mp = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
        }

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1+s2) != len(s3):
            return False

        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        dp[0][0] = True

        for i1 in range(1, len(s1) + 1):
            if dp[0][i1 - 1] and s1[i1 - 1] == s3[i1 - 1]:
                dp[0][i1] = True
        
        for i2 in range(1, len(s2) + 1):
            if dp[i2 - 1][0] and s2[i2 - 1] == s3[i2 - 1]:
                dp[i2][0] = True
        
        for i2 in range(1, len(s2) + 1):
            for i1 in range(1, len(s1) + 1):
                #插入新字符逻辑
                if dp[i2][i1 - 1] and s1[i1-1] == s3[i1 + i2-1]:
                    #s1增加逻辑
                    dp[i2][i1] = True
                elif dp[i2 - 1][i1] and s2[i2-1] == s3[i1 + i2-1]:
                    dp[i2][i1] = True
        
        return dp[-1][-1]
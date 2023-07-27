#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        # 创建二维dp数组，行数为石头的数量加1，列数为target加1
        # dp[i][j]表示前i个石头能否组成总重量为j
        dp = [[False] * (target + 1) for _ in range(len(stones) + 1)]
        
        # 初始化第一列，表示总重量为0时，前i个石头都能组成
        for i in range(len(stones) + 1):
            dp[i][0] = True
        
        for i in range(1, len(stones) + 1):
            for j in range(1, target + 1):
                # 如果当前石头重量大于当前目标重量j，则无法选择该石头
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 可选择该石头或不选择该石头
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]
        
        # 找到最大的重量i，使得dp[len(stones)][i]为True
        # 返回总重量减去两倍的最接近总重量一半的重量
        for i in range(target, -1, -1):
            if dp[len(stones)][i]:
                return total_sum - 2 * i
        
        return 0
# @lc code=end


#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cashPlan = [-1 for _ in range(amount + 1)]
        cashPlan[0] = 0
        for coin in coins:
            for value in range(amount+1):
                if value - coin >= 0 and cashPlan[value-coin] != -1:
                    if cashPlan[value] == -1:
                        cashPlan[value] = cashPlan[value-coin] + 1
                    else:
                        cashPlan[value] = min(cashPlan[value], cashPlan[value-coin] + 1)
        return cashPlan[-1]
# @lc code=end


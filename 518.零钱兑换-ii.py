#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cashBag = [0 for _ in range(amount + 1)]
        cashBag[0] = 1
        for item in coins:
            for money in range(amount + 1):
                if (money + item) <= amount:
                    cashBag[money + item] += cashBag[money]
        return cashBag[-1] 


# @lc code=end

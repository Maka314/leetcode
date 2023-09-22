#
# @lc app=leetcode.cn id=2591 lang=python3
# @lcpr version=21914
#
# [2591] Distribute Money to Maximum Children
#

# @lc code=start
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        res = 0
        money -= children
        if money < 0:
            return -1
        while money and res < children:
            # there are money left and kids waiting for money
            if money >= 7 and res <= children:
                # which you can add a kid get 8
                res += 1
                money -= 7
            elif money == 3:
                money -= 3
                if res == children-1:
                    res -= 1
            else:
                money -= money
        
        if money:
            res -= 1
        
        return res
# @lc code=end



#
# @lcpr case=start
# 20\n3\n
# @lcpr case=end

# @lcpr case=start
# 16\n2\n
# @lcpr case=end

# @lcpr case=start
# 60\n2\n
# @lcpr case=end

# @lcpr case=start
# 24\n3\n
# @lcpr case=end
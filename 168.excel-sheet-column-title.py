#
# @lc app=leetcode.cn id=168 lang=python3
# @lcpr version=21914
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = [0 for _ in range(7)]
        for n in range(6,-1,-1):
            currentMax = 26 ** n
            while currentMax <= columnNumber:
                columnNumber -= currentMax
                res[n] += 1
                
        return n

# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 28\n
# @lcpr case=end

# @lcpr case=start
# 701\n
# @lcpr case=end

# @lcpr case=start
# 2147483647\n
# @lcpr case=end

#


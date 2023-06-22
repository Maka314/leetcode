#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=21909
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pi = 0
        for si in range(len(s)):
            pi = 0
            flag = True
            while flag:
                if pi == len(p):
                    return True
                else:
                    pass
# @lc code=end



#
# @lcpr case=start
# "aa"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# @lcpr case=end

#


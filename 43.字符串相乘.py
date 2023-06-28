#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2 = 0,0
        for i1,j1 in enumerate(num1[::-1]):
            n1+=int(j1)*10**i1
        for i2,j2 in enumerate(num2[::-1]):
            n2+=int(j2)*10**i2
        res = n1*n2
        return str(res)
# @lc code=end


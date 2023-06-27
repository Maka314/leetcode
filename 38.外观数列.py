#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def countAndSay(n):
            res=""
            n = str(n)+'-'

            l,r = 0,0
            rMax = len(n)
            while r<rMax:
                if n[r] != n[l]:
                    res += str(r-l)
                    res += n[l]
                    l=r
                r+=1
            return res
        res = '1'
        for _ in range(n-1):
            res = countAndSay(res)
        return res
# @lc code=end


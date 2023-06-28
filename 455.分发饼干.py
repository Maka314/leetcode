#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i_s = len(s)-1
        res=0
        for ig in range(len(g)-1,-1,-1):
            if i_s == -1:
                break
            if g[ig]>s[i_s]:
                pass
            elif g[ig]<=s[i_s]:
                res+=1
                i_s-=1
        return res
# @lc code=end


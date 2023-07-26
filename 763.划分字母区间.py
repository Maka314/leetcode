#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lastP = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in lastP:
                lastP[s[i]] = i

        i = 0
        while i < len(s):
            endOfLine = lastP[s[i]]
            while i < endOfLine:
                endOfLine = max(lastP[s[i]],endOfLine)
                i += 1
            res.append(i)
            i += 1
        for i in range(len(res)-1,0,-1):
            res[i] = res[i] - res[i-1]
        res[0] += 1
        return res
# @lc code=end

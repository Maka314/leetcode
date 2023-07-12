#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = {}
        for c in words[0]:
            if c in res:
                res[c][0] += 1
            else:
                res[c] = [1,0]
        for w in words[1:]:
            for c in w:
                if c in res:
                    res[c][1] += 1
            for i in res:
                res[i][0] = min(res[i][0], res[i][1])
                res[i][1] = 0
        resL = []
        for i in res:
            for j in range(res[i][0]):
                resL.append(i)
        return resL
# @lc code=end


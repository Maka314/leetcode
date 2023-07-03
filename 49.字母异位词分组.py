#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            temp = list(strs[i])
            temp.sort()
            temp = ''.join(temp)
            if temp not in res:
                res[temp] = [strs[i]]
            else:
                res[temp].append(strs[i])
        return(list(res.values()))
# @lc code=end


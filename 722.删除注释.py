#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#


# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source = "\n".join(source)+'\n'
        tempRes = ""
        size = len(source)
        currentP = 0
        while currentP < size:
            if source[currentP : currentP + 2] == "/*":
                currentP = self.findTarget(source, currentP + 2, "*/")
            elif source[currentP : currentP + 2] == "//":
                currentP = self.findTarget(source, currentP + 2, "\n")
                tempRes += '\n'
            else:
                tempRes += source[currentP]
                currentP += 1
        res = tempRes.split("\n")
        i = 0
        while i < len(res):
            if res[i] == "":
                res.pop(i)
            else:
                i += 1
        return res

    def findTarget(self, source: str, start: int, target: str):
        targetLenth = len(target)
        for i in range(start, len(source)):
            if source[i : i + targetLenth] == target:
                return i + targetLenth


# @lc code=end

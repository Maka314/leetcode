#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.backTracking([], 0, s)
        return self.res

    def backTracking(self, path, startIndex, s):
        if startIndex == len(s):
            self.res.append(path[:])
            return

        path.append("")
        for i in range(startIndex, len(s)):
            path[-1] += s[i]
            if path[-1] == path[-1][::-1]:
                self.backTracking(path[:], i + 1, s)  # 注意参数的传递方式，只传递数组的话下层函数是能访问到递归第一层的


# @lc code=end

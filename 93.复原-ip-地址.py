#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.s = s
        self.res = []
        self.backTracking([], 0)
        return self.res

    def backTracking(self, path, startIndex):
        if startIndex == len(self.s):
            if len(path) == 4:
                self.res.append(".".join(path))
            return

        path.append("")
        upperBond = min(startIndex + 3, len(self.s))
        for i in range(startIndex, upperBond):
            path[-1] += self.s[i]
            if (len(path[-1]) > 1 and path[-1][0] == "0") or int(path[-1]) > 255:
                break
            self.backTracking(path[:],i+1)


# @lc code=end

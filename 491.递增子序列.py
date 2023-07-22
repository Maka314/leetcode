#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backTracking(0, [], nums)
        return self.res

    def backTracking(self, startIndex, path, nums):
        if len(path) >= 2:
            self.res.append(path[:])

        usedElement = set()
        for i in range(startIndex, len(nums)):
            if nums[i] in usedElement:
                continue
            usedElement.add(nums[i])
            path.append(nums[i])

            if len(path) == 1 or(len(path) > 1 and path[-1] >= path[-2]):
                self.backTracking(i + 1, path, nums)
            path.pop()
# @lc code=end


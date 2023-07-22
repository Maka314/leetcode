#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.backTracking([], 0, nums)
        return self.res

    def backTracking(self, path ,startIndex, nums):
        self.res.append(path[:])

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            if i > startIndex and nums[i] == nums[i-1]:
                path.pop()
                continue
            self.backTracking(path,i+1,nums)
            path.pop()
# @lc code=end


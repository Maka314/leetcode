#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backTracking([], 0, nums)
        return self.res
    
    def backTracking(self, path, startIndex, nums):
        self.res.append(path[:])

        for i in range(startIndex,len(nums)):
            path.append(nums[i])
            self.backTracking(path,i+1,nums)
            path.pop()
# @lc code=end


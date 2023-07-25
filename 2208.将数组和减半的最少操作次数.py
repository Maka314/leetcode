#
# @lc app=leetcode.cn id=2208 lang=python3
#
# [2208] 将数组和减半的最少操作次数
#

# @lc code=start
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        res, target = 0, sum(nums)/2
        s = 0
        searchArea = len(nums) - 1
        nums.sort()
        while s < target:
            biggetsI = searchArea
            for i in range(searchArea,len(nums)):
                if nums[i] > nums[biggetsI]:
                    biggetsI = i
            nums[biggetsI] = nums[biggetsI]/2
            s += nums[biggetsI]
            if biggetsI == searchArea:
                searchArea -= 1
            res += 1
        return res
# @lc code=end


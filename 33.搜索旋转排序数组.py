#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = -1,len(nums)
        while r-l>1:
            mid = round((l+r)/2)
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]:
                #前半段为单调增
                if nums[0]<=target and nums[mid]>=target:
                    r = mid
                else:
                    l = mid
            else:
                #后半段为单调增
                if nums[mid]<=target and nums[-1]>=target:
                    l = mid
                else:
                    r = mid
        return -1
# @lc code=end


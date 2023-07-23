#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, size = 0, len(height)
        while l < size - 1:
            higestIndex = l + 1
            for r in range(l + 1, size):
                if height[r] >= height[l]:
                    res += (r - l - 1) * height[l] - sum(height[l+1:r])
                    l = r
                    continue
                if height[r] > height[higestIndex]:
                    higestIndex = r
            if higestIndex>l:
                res += (higestIndex - l - 1) * height[higestIndex] - sum(height[l+1:higestIndex])
                l = higestIndex
        return res
# @lc code=end

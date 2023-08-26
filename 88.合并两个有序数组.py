#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp1 = nums1[:m]
        for i in range(len(nums1)):
            if temp1 and not nums2:
                nums1[i] = temp1.pop(0)
            elif not temp1 and nums2:
                nums1[i] = nums2.pop(0)
            elif temp1[0] > nums2[0]:
                nums1[i] = nums2.pop(0)
            else:
                nums1[i] = temp1.pop(0)
# @lc code=end


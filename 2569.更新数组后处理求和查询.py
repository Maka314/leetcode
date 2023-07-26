#
# @lc app=leetcode.cn id=2569 lang=python3
#
# [2569] 更新数组后处理求和查询
#


# @lc code=start
class Solution:
    def handleQuery(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        res = []
        for operation in queries:
            if operation[0] == 1:
                self.operation1(nums1, operation[1], operation[2])
                print(1, nums1)
            elif operation[0] == 2:
                self.operation2(nums1, nums2, operation[1])
                print(2, nums2)
            elif operation[0] == 3:
                res.append(sum(nums2))
        return res

    def operation1(self, nums, l, r):
        for i in range(l, r + 1):
            if not nums[i]:
                nums[i] = 1
            elif nums[i] == 1:
                nums[i] = 0

    def operation2(self, nums1, nums2, p):
        for i in range(len(nums1)):
            nums2[i] += nums1[i] * p


# @lc code=end

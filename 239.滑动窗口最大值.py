#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n=len(nums)
        q=deque()
        ans = []
        for i,c in enumerate(nums):
            while q and nums[q[-1]]<c:  # 队首
                q.pop()
            # 当前位置为i, 最后一个有效位 i-k+1
            while q and q[0]<i-k+1:  # 队尾
                mx=q.popleft()
            q.append(i)
            if i+1>=k:
                ans.append(nums[q[0]])
        return ans
# @lc code=end


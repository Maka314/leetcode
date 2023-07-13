#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class sortQueue:
    def __init__(self) -> None:
        self.queue = []
    
    def push(self, v):
        while self.queue and v > self.queue[-1]:
            self.queue.pop()
        self.queue.append(v)
    
    def top(self):
        if self.queue:
            return self.queue[0]
        else:
            return None
    
    def pop(self):
        return self.queue.pop(0)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = sortQueue()
        for c in nums[:k]:
            queue.push(c)
        res = [queue.top()]
        for i in range(k,len(nums)):
            if nums[i-k] == queue.top():
                queue.pop()
            queue.push(nums[i])
            res.append(queue.top())
        return res
# @lc code=end


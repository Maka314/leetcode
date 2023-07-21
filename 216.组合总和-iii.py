#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#


# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.backtracking([], 0, 1, k, n)
        return self.res

    def backtracking(self, queue, qSum, startIndex, k, n):
        if qSum > n:
            return
        if len(queue) == k:
            if qSum == n:
                self.res += [queue[:]]
            return
        for i in range(startIndex, 9 - (k - len(queue)) + 2):
            queue.append(i)
            qSum += i
            self.backtracking(queue, qSum, i + 1, k, n)
            qSum -= i
            queue.pop()


# @lc code=end

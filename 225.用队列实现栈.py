#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.temp.append(self.queue.pop(0))
        res = self.queue.pop(0)
        while self.temp:
            self.queue.append(self.temp.pop(0))
        return res

    def top(self) -> int:
        while len(self.queue) > 1:
            self.temp.append(self.queue.pop(0))
        res = self.queue.pop(0)
        self.temp.append(res)
        while self.temp:
            self.queue.append(self.temp.pop(0))
        return res

    def empty(self) -> bool:
        res = (len(self.queue) == 0)
        return res

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end


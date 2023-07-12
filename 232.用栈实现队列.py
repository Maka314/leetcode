#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.temp.append(self.stack.pop())
        res = self.temp.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return res

    def peek(self) -> int:
        while self.stack:
            self.temp.append(self.stack.pop())
        res = self.temp[-1]
        while self.temp:
            self.stack.append(self.temp.pop())
        return res

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end


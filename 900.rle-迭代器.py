#
# @lc app=leetcode.cn id=900 lang=python3
#
# [900] RLE 迭代器
#

# @lc code=start
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding

    def next(self, n: int) -> int:
        res = -1
        while self.encoding and n > 0:
            if n == self.encoding[0]:
                res = self.encoding[1]
                self.encoding.pop(0)
                self.encoding.pop(0)
            elif n > self.encoding[0]:
                n -= self.encoding[0]
                self.encoding.pop(0)
                self.encoding.pop(0)
            else:
                self.encoding[0] -= n
                res = self.encoding[1]
        return res

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
# @lc code=end


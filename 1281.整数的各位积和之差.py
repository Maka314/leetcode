class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s1, s2 = 1,0
        while n:
            s1 *= n % 10
            s2 += n % 10
            n = n // 10
        return s1 - s2
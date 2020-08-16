class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        bases = (2, 3, 5)
        for b in bases:
            while num % b == 0:
                num //= b

        if num == 1:
            return True
        else:
            return False

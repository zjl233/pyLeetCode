class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 如果 pattern 耗尽，并且 s 没有耗尽，匹配失败
        if not p and s:
            return False

        # 如果 patter 和 s 都耗尽了，匹配成功
        if not s and not p:
            return True

        if p[0] == '.':
            return self.isMatch(s[1:], p[1:])

        if s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])
        else:
            ...
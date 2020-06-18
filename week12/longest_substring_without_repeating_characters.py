class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 0
        st = set()
        maxlen = r - l  # 滑动窗口为 左闭右开区间

        while r < len(s):
            if s[r] not in st:
                st.add(s[r])
                r += 1
                maxlen = max(maxlen, r - l)
            else:
                st.remove(s[l])
                l += 1

        return maxlen


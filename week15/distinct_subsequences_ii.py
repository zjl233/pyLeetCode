class Solution:
    def distinctSubseqII(self, S: str) -> int:
        # 在 ch 加入到 all 之前，all 的长度
        # ch 加入 all 中的每一个序列之后，生成新的序列
        # 同时要减去之前重复使用的序列
        prev_alls = [0 for _ in range(26)]
        all_ = 1  # 不管最后算不算空集，这里先放空个空字符串
        for ch in S:
            # 之前加入 ch 字符时，序列有多长
            # 注：不是加入 ch 字符，导致序列增加了多少
            prev_all = prev_alls[ord(ch) - ord('a')]
            # 这一次加入 ch 字符值，序列有所长，保存起来
            prev_alls[ord(ch) - ord('a')] = all_
            all_ += (all_ - prev_all)

        # return all_  # 空字符串也算
        # return all_ - 1  # 空字符串不算
        return (all_ - 1) % (10 ** 9 + 7)  # 空字符串不算

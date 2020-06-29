def longest_common_substring(text1: str, text2: str) -> int:
    h, w = len(text1), len(text2)
    dp = [[0 for _ in range(w)] for _ in range(h)]

    max_ = 0
    for i in range(0, h):
        for j in range(0, w):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + (dp[i - 1][j - 1] if (i > 0 and j > 0) else 0)
            max_ = max(max_, dp[i][j])
    return max_


def oj_main():
    str1 = input()
    str2 = input()
    res = longest_common_substring(str1, str2)
    print(res)


if __name__ == '__main__':
    oj_main()

if __name__ == '__main__':

    import sys

    for line in sys.stdin:
        s = line.replace('\n', '')
        source = list(s)
        # print(source, 'len:', len(source))
        strs = list(filter(str.isalpha, source))
        strs.sort(key=str.casefold)
        j = 0
        for i in range(len(s)):
            if str.isalpha(source[i]):
                source[i] = strs[j]
                j += 1
        print(''.join(source))

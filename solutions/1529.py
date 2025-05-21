class Solution:
    def maxDiff(self, num):
        s = str(num)

        # Maximize: replace first non-9 digit with 9
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else:
            max_num = num

        # Minimize: replace first digit (if not 1) with 1, or else replace any non-0 (not first) with 0
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    min_num = int(s.replace(ch, '0'))
                    break
            else:
                min_num = num

        return max_num - min_num

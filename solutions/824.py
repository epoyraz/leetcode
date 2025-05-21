class Solution(object):
    def numberOfLines(self, widths, s):
        lines = 1
        curr_width = 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            if curr_width + w > 100:
                lines += 1
                curr_width = w
            else:
                curr_width += w
        return [lines, curr_width]

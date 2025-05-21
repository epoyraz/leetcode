class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        line = []
        line_len = 0

        for word in words:
            if line_len + len(line) + len(word) > maxWidth:
                for i in range(maxWidth - line_len):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line = []
                line_len = 0
            line.append(word)
            line_len += len(word)

        res.append(' '.join(line).ljust(maxWidth))
        return res

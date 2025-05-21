class Solution(object):
    def placeWordInCrossword(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def can_place(segment, word):
            if len(segment) != len(word):
                return False
            for s, w in zip(segment, word):
                if s != ' ' and s != w:
                    return False
            return True

        def check_lines(lines):
            for line in lines:
                i = 0
                while i < len(line):
                    if line[i] == '#':
                        i += 1
                        continue
                    j = i
                    while j < len(line) and line[j] != '#':
                        j += 1
                    segment = line[i:j]
                    if can_place(segment, word) or can_place(segment, word[::-1]):
                        return True
                    i = j
            return False

        # Rows as-is and reversed
        rows = board
        cols = list(zip(*board))  # transpose for columns

        return check_lines(rows) or check_lines(cols)

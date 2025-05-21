class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        res = []
        in_block = False
        buf = []
        
        for line in source:
            i = 0
            if not in_block:
                buf = []
            while i < len(line):
                if in_block:
                    # Look for end of block comment
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    # Not in block
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        in_block = True
                        i += 2
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        # Line comment: ignore rest of line
                        break
                    else:
                        buf.append(line[i])
                        i += 1
            # After processing line, if not in block and buffer non-empty, flush
            if not in_block and buf:
                res.append("".join(buf))
        return res

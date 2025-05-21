class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        MOD = 10**9+7
        n = len(code)
        stack = []
        i = 0

        # Must start with an opening tag
        if n < 7 or code[0] != '<' or code[1] in ('/', '!'):
            return False

        while i < n:
            if code[i] != '<':
                # text outside any open tag is invalid
                if not stack:
                    return False
                i += 1
                continue

            # CDATA section
            if i + 9 <= n and code[i:i+9] == '<![CDATA[':
                if not stack:
                    return False
                j = code.find(']]>', i+9)
                if j < 0:
                    return False
                i = j + 3

            # Closing tag
            elif i + 2 < n and code[i+1] == '/':
                j = code.find('>', i+2)
                if j < 0:
                    return False
                tagname = code[i+2:j]
                # stricter check: only AâZ letters, length 1â9
                if not (1 <= len(tagname) <= 9 and tagname.isalpha() and tagname.isupper()):
                    return False
                # must match the top of the stack
                if not stack or stack[-1] != tagname:
                    return False
                stack.pop()
                i = j + 1
                # if we've just closed the root, we must be at the very end
                if not stack and i != n:
                    return False

            # Opening tag
            else:
                j = code.find('>', i+1)
                if j < 0:
                    return False
                tagname = code[i+1:j]
                if not (1 <= len(tagname) <= 9 and tagname.isalpha() and tagname.isupper()):
                    return False
                stack.append(tagname)
                i = j + 1

        # all tags should be closed
        return not stack

class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        stack = []

        for ch in expression:
            if ch == ',':
                continue
            elif ch == ')':
                vals = set()
                while stack[-1] != '(':
                    vals.add(stack.pop())
                stack.pop()  # remove '('
                op = stack.pop()
                if op == '&':
                    stack.append('t' if all(v == 't' for v in vals) else 'f')
                elif op == '|':
                    stack.append('t' if any(v == 't' for v in vals) else 'f')
                elif op == '!':
                    stack.append('f' if list(vals)[0] == 't' else 't')
            else:
                stack.append(ch)

        return stack[0] == 't'

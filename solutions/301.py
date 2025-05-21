class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import deque

        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = set([s])
        result = []
        found = False

        while queue:
            current = queue.popleft()
            if is_valid(current):
                result.append(current)
                found = True
            if found:
                continue
            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                next_str = current[:i] + current[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)

        return result

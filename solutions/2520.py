class Solution(object):
    def robotWithString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # Precompute suffix minimum characters
        # suffix_min[i] = min(s[i], s[i+1], ..., s[n-1])
        suffix_min = [''] * (n + 1)
        suffix_min[n] = '{'  # character after 'z' in ASCII
        for i in range(n - 1, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])

        t_stack = []
        result = []

        for i, ch in enumerate(s):
            # Operation 1: push from s to t
            t_stack.append(ch)
            # Operation 2: pop from t to result while optimal
            # We pop while the top of t_stack <= min of remaining s
            while t_stack and t_stack[-1] <= suffix_min[i + 1]:
                result.append(t_stack.pop())

        # Flush remaining from t_stack
        while t_stack:
            result.append(t_stack.pop())

        return ''.join(result)

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        # Decide which pattern to remove first
        if x >= y:
            first, first_score = "ab", x
            second, second_score = "ba", y
        else:
            first, first_score = "ba", y
            second, second_score = "ab", x

        total = 0
        stack = []

        # First pass: remove all occurrences of `first`
        for c in s:
            stack.append(c)
            if len(stack) >= 2 and stack[-2] + stack[-1] == first:
                # pop the two characters, gain score
                stack.pop()
                stack.pop()
                total += first_score

        # Build the intermediate string
        t = "".join(stack)

        # Second pass: remove all occurrences of `second`
        stack = []
        for c in t:
            stack.append(c)
            if len(stack) >= 2 and stack[-2] + stack[-1] == second:
                stack.pop()
                stack.pop()
                total += second_score

        return total

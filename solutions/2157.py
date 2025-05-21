class Solution(object):
    def smallestSubsequence(self, s, k, letter, repetition):
        """
        :type s: str
        :type k: int
        :type letter: str
        :type repetition: int
        :rtype: str
        """
        n = len(s)
        total_letter = 0
        for ch in s:
            if ch == letter:
                total_letter += 1

        stack = []
        count_letter_in_stack = 0

        for i in range(n):
            ch = s[i]
            remaining = n - i - 1

            while stack and ch < stack[-1] and \
                  len(stack) + remaining >= k:
                # Only pop if:
                # - We don't violate repetition constraint
                top = stack[-1]
                if top == letter:
                    if count_letter_in_stack + total_letter - 1 < repetition:
                        break
                    count_letter_in_stack -= 1
                stack.pop()

            if len(stack) < k:
                if ch == letter:
                    stack.append(ch)
                    count_letter_in_stack += 1
                else:
                    # Only push non-letter if we can still fit enough letters
                    if (k - len(stack)) > (repetition - count_letter_in_stack):
                        stack.append(ch)

            if ch == letter:
                total_letter -= 1

        return ''.join(stack)

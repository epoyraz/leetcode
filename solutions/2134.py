class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        def max_length(ch):
            left = 0
            count = 0
            max_len = 0
            for right in range(len(answerKey)):
                if answerKey[right] != ch:
                    count += 1
                while count > k:
                    if answerKey[left] != ch:
                        count -= 1
                    left += 1
                max_len = max(max_len, right - left + 1)
            return max_len

        return max(max_length('T'), max_length('F'))

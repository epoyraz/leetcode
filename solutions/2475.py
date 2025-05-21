class Solution(object):
    def largestPalindromic(self, num):
        from collections import Counter

        count = Counter(num)
        half = []
        mid = ''

        for d in reversed('0123456789'):
            pairs = count[d] // 2
            if pairs > 0:
                half.extend([d] * pairs)
                count[d] -= 2 * pairs

        for d in reversed('0123456789'):
            if count[d] > 0:
                mid = d
                break

        while half and half[0] == '0':
            half.pop(0)

        if not half and not mid:
            return '0'

        return ''.join(half) + mid + ''.join(reversed(half))

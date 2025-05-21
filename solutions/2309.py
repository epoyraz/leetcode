class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        a, b = pattern[0], pattern[1]

        # Count subsequences of pattern in original text
        count_a = count_b = res = 0
        for ch in text:
            if ch == b:
                res += count_a
                count_b += 1
            if ch == a:
                count_a += 1

        # Try adding pattern[0] at the front OR pattern[1] at the end
        # Whichever gives more new subsequences
        return res + max(text.count(b), text.count(a))

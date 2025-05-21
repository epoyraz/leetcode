class Solution(object):
    def countLargestGroup(self, n):
        from collections import Counter

        def digit_sum(x):
            return sum(int(d) for d in str(x))

        count = Counter(digit_sum(i) for i in range(1, n + 1))
        max_size = max(count.values())
        return sum(1 for v in count.values() if v == max_size)

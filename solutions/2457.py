class Solution(object):
    def countSpecialNumbers(self, n):
        digits = list(map(int, str(n)))
        length = len(digits)
        res = 0

        # Count special numbers with length less than len(n)
        for i in range(1, length):
            count = 9
            available = 9
            for j in range(i - 1):
                count *= available
                available -= 1
            res += count

        # Count special numbers with same length as n
        seen = set()
        for i in range(length):
            for d in range(0 if i else 1, digits[i]):
                if d in seen:
                    continue
                count = 1
                available = 9 - i
                for j in range(i + 1, length):
                    count *= available
                    available -= 1
                res += count
            if digits[i] in seen:
                break
            seen.add(digits[i])
        else:
            res += 1

        return res

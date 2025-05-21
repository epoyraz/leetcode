class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1
        count = 1  # one '1' in the initial "122"

        while len(s) < n:
            times = s[i]
            s.extend([num] * times)
            if num == 1:
                count += min(n - len(s) + times, times)
            num ^= 3  # toggle between 1 and 2
            i += 1

        return count

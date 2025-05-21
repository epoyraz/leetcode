
class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        n = min(len(s1), len(s2), len(s3))
        common_len = 0

        for i in range(n):
            if s1[i] == s2[i] == s3[i]:
                common_len += 1
            else:
                break

        if common_len == 0:
            return -1

        return (len(s1) - common_len) + (len(s2) - common_len) + (len(s3) - common_len)

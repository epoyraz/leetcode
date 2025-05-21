class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Counts the number of substrings where the number of '0's is at most k
        or the number of '1's is at most k.
        """
        n = len(s)
        result = 0
        # Enumerate all starting positions
        for i in range(n):
            zeros = 0
            ones = 0
            # Expand the substring from i to j
            for j in range(i, n):
                if s[j] == '0':
                    zeros += 1
                else:
                    ones += 1
                # If both counts exceed k, further extensions cannot satisfy the constraint
                if zeros > k and ones > k:
                    break
                # Otherwise, this substring [i:j+1] is valid
                result += 1
        return result

# Example usage:
# sol = Solution()
# print(sol.countKConstraintSubstrings("10101", 1))     # 12
# print(sol.countKConstraintSubstrings("1010101", 2))  # 25
# print(sol.countKConstraintSubstrings("11111", 1))     # 15

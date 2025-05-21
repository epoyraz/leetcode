class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # custom gcd to support older Python versions
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_num = max(nums)
        present = [False] * (max_num + 1)
        for x in nums:
            present[x] = True

        count = 0
        # for each possible gcd g
        for g in range(1, max_num + 1):
            current_gcd = 0
            # iterate multiples of g
            for multiple in range(g, max_num + 1, g):
                if present[multiple]:
                    val = multiple // g
                    current_gcd = val if current_gcd == 0 else gcd(current_gcd, val)
                    # early exit: if gcd becomes 1, g is achievable
                    if current_gcd == 1:
                        count += 1
                        break
        return count

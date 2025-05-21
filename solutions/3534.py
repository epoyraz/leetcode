class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Two numbers are almost equal if one swap within the digits of one number (at most once) can make them equal, allowing leading zeros.
        Brute-force each pair with up to O(d^2) swaps, total O(n^2 d^2) for n<=100, d<=7.
        """
        def can_swap_to(a_str, target):
            # Try every swap of two positions in a_str to match target int
            n = len(a_str)
            for i in range(n):
                for j in range(i+1, n):
                    lst = list(a_str)
                    lst[i], lst[j] = lst[j], lst[i]
                    # strip leading zeros
                    s = ''.join(lst).lstrip('0')
                    if not s:
                        val = 0
                    else:
                        val = int(s)
                    if val == target:
                        return True
            return False

        count = 0
        n = len(nums)
        # Precompute strings
        str_nums = [str(x) for x in nums]
        for i in range(n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                if a == b:
                    count += 1
                else:
                    # try swap in a to get b
                    if can_swap_to(str_nums[i], b):
                        count += 1
                    # else try swap in b to get a
                    elif can_swap_to(str_nums[j], a):
                        count += 1
        return count
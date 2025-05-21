class Solution(object):
    def getMinSwaps(self, num, k):
        # compute the k-th next permutation (the k-th smallest wonderful integer)
        t = list(num)
        for _ in range(k):
            # next_permutation on t
            i = len(t) - 2
            while i >= 0 and t[i] >= t[i+1]:
                i -= 1
            # swap pivot with next larger element
            j = len(t) - 1
            while j > i and t[j] <= t[i]:
                j -= 1
            t[i], t[j] = t[j], t[i]
            # reverse suffix
            t[i+1:] = reversed(t[i+1:])
        # count adjacent swaps to turn num into that target
        s_list = list(num)
        ans = 0
        n = len(s_list)
        for i in range(n):
            if s_list[i] == t[i]:
                continue
            # find the target digit in s_list
            j = i + 1
            while s_list[j] != t[i]:
                j += 1
            # bring it to position i by swapping adjacent digits
            while j > i:
                s_list[j], s_list[j-1] = s_list[j-1], s_list[j]
                ans += 1
                j -= 1
        return ans

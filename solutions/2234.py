from bisect import bisect_right

class Solution:
    def kIncreasing(self, arr, k):
        def lnds(seq):
            stack = []
            for num in seq:
                idx = bisect_right(stack, num)
                if idx == len(stack):
                    stack.append(num)
                else:
                    stack[idx] = num
            return len(stack)

        n = len(arr)
        operations = 0

        for start in range(k):
            seq = [arr[i] for i in range(start, n, k)]
            operations += len(seq) - lnds(seq)

        return operations

class Solution(object):
    def findMinFibonacciNumbers(self, k):
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        count = 0
        for i in reversed(fib):
            if k >= i:
                k -= i
                count += 1
            if k == 0:
                break

        return count

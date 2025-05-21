class Solution(object):
    def sumFourDivisors(self, nums):
        def getDivisors(n):
            divs = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)
                if len(divs) > 4:
                    return 0
            return sum(divs) if len(divs) == 4 else 0

        return sum(getDivisors(num) for num in nums)

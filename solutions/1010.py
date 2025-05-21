class Solution:
    def powerfulIntegers(self, x, y, bound):
        result = set()
        i = 0
        while x ** i <= bound:
            j = 0
            while y ** j <= bound:
                val = x ** i + y ** j
                if val <= bound:
                    result.add(val)
                else:
                    break
                if y == 1:
                    break
                j += 1
            if x == 1:
                break
            i += 1
        return list(result)

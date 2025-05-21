class Solution(object):
    def maximumPopulation(self, logs):
        arr = [0] * 101
        for b, d in logs:
            arr[b - 1950] += 1
            arr[d - 1950] -= 1
        curr = 0
        max_pop = 0
        year = 1950
        for i in range(101):
            curr += arr[i]
            if curr > max_pop:
                max_pop = curr
                year = 1950 + i
        return year

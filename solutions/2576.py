class Solution(object):
    def bestClosingTime(self, customers):
        penalN = 0
        penalY = customers.count('Y')
        minPen = float('inf')
        ans = 0
        n = len(customers)
        for j in range(n + 1):
            cur = penalN + penalY
            if cur < minPen:
                minPen = cur
                ans = j
            if j < n:
                if customers[j] == 'N':
                    penalN += 1
                else:
                    penalY -= 1
        return ans

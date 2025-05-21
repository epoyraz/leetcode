class Solution:
    def removeDigit(self, number, digit):
        best = ""
        for i, ch in enumerate(number):
            if ch == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > best:
                    best = candidate
        return best

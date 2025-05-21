class Solution:
    def divisorSubstrings(self, num, k):
        s = str(num)
        count = 0
        for i in range(len(s) - k + 1):
            sub = s[i:i+k]
            val = int(sub)
            if val != 0 and num % val == 0:
                count += 1
        return count

class Solution:
    def subStrHash(self, s, power, modulo, k, hashValue):
        n = len(s)
        result = n - k
        current_hash = 0
        power_k = pow(power, k, modulo)

        def val(ch):
            return ord(ch) - ord('a') + 1

        for i in range(n - 1, -1, -1):
            current_hash = (current_hash * power + val(s[i])) % modulo

            if i + k < n:
                current_hash = (current_hash - val(s[i + k]) * power_k) % modulo

            if i + k <= n and current_hash == hashValue:
                result = i

        return s[result:result + k]

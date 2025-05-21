class Solution:
    def decode(self, encoded):
        n = len(encoded) + 1
        total_xor = 0
        for i in range(1, n + 1):
            total_xor ^= i
        odd_xor = 0
        for i in range(1, len(encoded), 2):
            odd_xor ^= encoded[i]
        first = total_xor ^ odd_xor
        perm = [first]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm

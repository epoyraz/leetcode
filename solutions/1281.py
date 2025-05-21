class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        # Prefix XOR bitmasks: 26-bit int where bit i = parity (odd/even) of letter 'a' + i
        prefix = [0] * (n + 1)
        
        for i in range(n):
            bit = 1 << (ord(s[i]) - ord('a'))
            prefix[i + 1] = prefix[i] ^ bit

        def count_odd(mask):
            return bin(mask).count('1')

        result = []
        for left, right, k in queries:
            mask = prefix[right + 1] ^ prefix[left]
            odd_count = count_odd(mask)
            result.append(odd_count // 2 <= k)
        
        return result

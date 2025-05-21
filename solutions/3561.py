import itertools
from collections import defaultdict, deque

class Solution(object):
    def kthCharacter(self, k, operations):
        """
        :type k: int
        :type operations: List[int]
        :rtype: str
        """
        # Number of operations
        m = len(operations)
        # Precompute the length of the string after each operation: length[i] = 2^i
        lengths = [1] * (m + 1)
        for i in range(m):
            lengths[i + 1] = lengths[i] << 1
        # Current position we want, and the total shift count
        cur_k = k
        shift_count = 0
        # Walk operations in reverse to map cur_k back to the original 'a'
        for i in range(m - 1, -1, -1):
            if cur_k > lengths[i]:
                # We're in the second half of the string after operation i
                cur_k -= lengths[i]
                # If this operation was a shift-append, accumulate one shift
                if operations[i] == 1:
                    shift_count = (shift_count + 1) % 26
        # After reversing all operations, we land at position cur_k in the initial string "a"
        # Since the initial word is "a" of length 1, cur_k must be 1
        # Apply the accumulated shifts to 'a'
        return chr((ord('a') - ord('a') + shift_count) % 26 + ord('a'))

    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = 0
        # Try all permutations of the three numbers
        for perm in itertools.permutations(nums):
            # Concatenate binary representations without leading zeros
            s = ''.join(bin(x)[2:] for x in perm)
            # Convert concatenated binary string to integer
            val = int(s, 2)
            if val > max_val:
                max_val = val
        return max_val

    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Build graph from method to the methods it invokes
        graph = defaultdict(list)
        for a, b in invocations:
            graph[a].append(b)
        # Find all suspicious methods reachable from k
        suspicious = set([k])
        dq = deque([k])
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if v not in suspicious:
                    suspicious.add(v)
                    dq.append(v)
        # Check for invocations into suspicious from outside
        for a, b in invocations:
            if b in suspicious and a not in suspicious:
                # Removal not possible
                return list(range(n))
        # Removal possible: return methods not in suspicious
        return [i for i in range(n) if i not in suspicious]

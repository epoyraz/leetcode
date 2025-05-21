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

class Solution(object):
    def maxPartitionsAfterOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        memo = {}
        n = len(s)
        
        def dp(idx, used_mask, can_change):
            """
            idx: current position in string
            used_mask: bitmask of characters in current partition
            can_change: whether we can still change one character
            """
            # Base case: End of string
            if idx == n:
                return 1
                
            # Check if already calculated
            state = (idx, used_mask, can_change)
            if state in memo:
                return memo[state]
                
            # Current character
            curr_char = ord(s[idx]) - ord('a')
            curr_bit = 1 << curr_char
            new_mask = used_mask | curr_bit
            distinct_count = bin(new_mask).count('1')
            
            # Option 1: Keep current character
            if distinct_count <= k:
                # Continue with current partition
                result = dp(idx + 1, new_mask, can_change)
            else:
                # Start a new partition
                result = 1 + dp(idx + 1, curr_bit, can_change)
                
            # Option 2: Change current character (if allowed)
            if can_change:
                max_with_change = 0
                
                # Try changing to all possible characters (except current)
                for new_char in range(26):
                    if new_char == curr_char:
                        continue
                        
                    # Calculate new mask with changed character
                    change_bit = 1 << new_char
                    change_mask = used_mask | change_bit
                    change_distinct = bin(change_mask).count('1')
                    
                    if change_distinct <= k:
                        # Continue current partition with changed character
                        max_with_change = max(max_with_change, dp(idx + 1, change_mask, False))
                    else:
                        # Start new partition with changed character
                        max_with_change = max(max_with_change, 1 + dp(idx + 1, change_bit, False))
                
                result = max(result, max_with_change)
                
            # Memoize and return
            memo[state] = result
            return result
            
        return dp(0, 0, True)
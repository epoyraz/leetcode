import sys

class Solution(object):
    def countNumbers(self, l_str, r_str, b):
        self.MOD = 10**9 + 7
        self.memo = {}  # Memoization table for DP states
        self.base_for_dp = 0  # Stores the current base 'b' for access in _actual_solve
        
        # It's good practice to ensure recursion limit is sufficient.
        # Python's default is often 1000. Max recursion depth is number of digits in base b,
        # which can be up to ~333 for b=2 and a 100-digit base-10 number. This should be fine.
        # current_recursion_limit = sys.getrecursionlimit()
        # required_limit = 400 # Max digits in base b + some buffer
        # if current_recursion_limit < required_limit:
        #    sys.setrecursionlimit(required_limit)


        count_r = self._get_count_le_s(r_str, b)
        
        l_val = int(l_str)
        l_minus_1_val = l_val - 1
        
        # Since l_str >= "1", l_val >= 1, so l_minus_1_val >= 0.
        # str(l_minus_1_val) will correctly convert this non-negative integer to string.
        count_l_minus_1 = self._get_count_le_s(str(l_minus_1_val), b)

        result = (count_r - count_l_minus_1 + self.MOD) % self.MOD
        return result

    def _int_to_base_b_digits(self, n_val, base):
        if n_val == 0:
            return [0]
        
        digits = []
        while n_val > 0:
            digits.append(n_val % base)
            n_val //= base # Integer division (works in Python 2 and 3)
        return digits[::-1] # Return digits in correct order (MSD first)

    def _actual_solve(self, s_digits_b, pos, prev_d, tight, is_started, n_total_digits):
        # Tuple for memoization key
        state = (pos, prev_d, tight, is_started)
        
        if pos == n_total_digits:
            # Successfully constructed a number of n_total_digits.
            # This counts one valid number. If is_started remained False, it means
            # all digits were zero, so this counts the number 0.
            return 1
        
        if state in self.memo:
            return self.memo[state]

        ans = 0
        # Determine the upper limit for the current digit based on 'tight' constraint
        limit = s_digits_b[pos] if tight else (self.base_for_dp - 1)

        for digit in range(limit + 1): # Iterate through possible values for the current digit
            # Update 'tight' for the next recursive call
            current_new_tight = tight and (digit == limit)
            
            if not is_started:
                # If we haven't placed any non-zero digit yet
                if digit == 0:
                    # If current digit is 0, we are still forming leading zeros (or the number 0)
                    # 'prev_d' for next step is 0 (or any value, it's ignored), 'is_started' remains False
                    ans = (ans + self._actual_solve(s_digits_b, pos + 1, 0, current_new_tight, False, n_total_digits)) % self.MOD
                else:
                    # This is the first non-zero digit
                    # 'prev_d' for next step is this 'digit', 'is_started' becomes True
                    ans = (ans + self._actual_solve(s_digits_b, pos + 1, digit, current_new_tight, True, n_total_digits)) % self.MOD
            else:
                # If we have already started (placed a non-zero digit)
                # The current digit must be greater than or equal to the previous digit
                if digit >= prev_d:
                    # 'prev_d' for next step is this 'digit', 'is_started' remains True
                    ans = (ans + self._actual_solve(s_digits_b, pos + 1, digit, current_new_tight, True, n_total_digits)) % self.MOD
        
        self.memo[state] = ans
        return ans

    def _get_count_le_s(self, num_str_base10, base_val):
        num_val = int(num_str_base10)
        
        s_digits_b_repr = self._int_to_base_b_digits(num_val, base_val)
        n_digits_in_s = len(s_digits_b_repr)
        
        self.memo.clear()  # Clear memo for each new upper bound S
        self.base_for_dp = base_val # Make base available to _actual_solve via self
        
        # Initial call to the recursive DP solver:
        # pos = 0 (start from the most significant digit)
        # prev_d = 0 (placeholder, effectively ignored since is_started is False)
        # tight = True (digits are restricted by S's digits initially)
        # is_started = False (we haven't placed any non-zero digit yet)
        count = self._actual_solve(s_digits_b_repr, 0, 0, True, False, n_digits_in_s)
        return count
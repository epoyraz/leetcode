import collections

class Solution(object):
    # Class-level variables for precomputation, initialized once.
    _precomputed_factors_done = False
    d_factors_static = []  # Stores (c2,c3,c5,c7) for each digit 0-9
    target_sum_factors_static = [] # Stores (sc2,sc3,sc5,sc7, has_other_prime_factor) for sums

    # Caps for prime factor counts in product P, based on max requirements for any sum S <= 81
    C2_CAP = 6  # Max exponent for 2 in S (S=64 -> 2^6)
    C3_CAP = 4  # Max exponent for 3 in S (S=81 -> 3^4)
    C5_CAP = 2  # Max exponent for 5 in S (S=25,50,75 -> 5^2)
    C7_CAP = 2  # Max exponent for 7 in S (S=49 -> 7^2)
    
    # Max sum of digits for a number < 10^9 (at most 9 digits like 999,999,999) is 9*9 = 81.
    MAX_SUM_DIGITS = 81

    def _get_digit_prime_factors(self, digit):
        # Manually provide factors for digits 0-9 for efficiency
        if digit == 0: return (0,0,0,0)
        if digit == 1: return (0,0,0,0)
        if digit == 2: return (1,0,0,0)
        if digit == 3: return (0,1,0,0)
        if digit == 4: return (2,0,0,0)
        if digit == 5: return (0,0,1,0)
        if digit == 6: return (1,1,0,0)
        if digit == 7: return (0,0,0,1)
        if digit == 8: return (3,0,0,0)
        if digit == 9: return (0,2,0,0)
        return (0,0,0,0) # Should not happen

    def _get_target_sum_prime_factors(self, S):
        if S == 0: return (0,0,0,0, False) # Sum 0 not for positive integers
        
        sc2,sc3,sc5,sc7 = 0,0,0,0
        has_other_prime = False
        
        temp_S = S
        while temp_S > 0 and temp_S % 2 == 0: sc2+=1; temp_S //= 2
        while temp_S > 0 and temp_S % 3 == 0: sc3+=1; temp_S //= 3
        while temp_S > 0 and temp_S % 5 == 0: sc5+=1; temp_S //= 5
        while temp_S > 0 and temp_S % 7 == 0: sc7+=1; temp_S //= 7
        
        if temp_S > 1: has_other_prime = True # Remaining temp_S has prime factors > 7
        return (sc2,sc3,sc5,sc7, has_other_prime)

    def _ensure_precomputation(self):
        if Solution._precomputed_factors_done:
            return

        Solution.d_factors_static = [self._get_digit_prime_factors(d) for d in range(10)]
        
        Solution.target_sum_factors_static.append((0,0,0,0,False)) # For sum = 0
        for s_val in range(1, Solution.MAX_SUM_DIGITS + 1): 
            Solution.target_sum_factors_static.append(self._get_target_sum_prime_factors(s_val))
        
        Solution._precomputed_factors_done = True

    # Instance variables for a single _solve_N call context
    # self.memo, self.snum_str, self.D
    
    def _dp(self, idx, current_sum, pc2, pc3, pc5, pc7, tight, is_leading, has_zero):
        state = (idx, current_sum, pc2, pc3, pc5, pc7, tight, is_leading, has_zero)
        if state in self.memo:
            return self.memo[state]

        if idx == self.D: # All digits placed
            if is_leading: # Number was "0" or "00" etc. Not positive.
                return 0
            
            # current_sum will be > 0 if not is_leading. Smallest positive number is 1 (sum=1).
            # An explicit check 'if current_sum == 0: return 0' is redundant here because
            # is_leading=False implies current_sum > 0.
            
            if has_zero: # Product of digits P is 0
                # 0 % current_sum == 0 is true, since current_sum > 0 for any valid number.
                return 1 
            
            # Product P is not zero. Check divisibility P % S == 0.
            s_sc2, s_sc3, s_sc5, s_sc7, s_has_other_prime = Solution.target_sum_factors_static[current_sum]
            
            if s_has_other_prime:
                # P (non-zero) has only 2,3,5,7 factors. Sum S has other factor(s) > 7. S cannot divide P.
                return 0 
            
            # Sum S has only 2,3,5,7 factors. Check if P has enough of these factors.
            if pc2 < s_sc2: return 0
            if pc3 < s_sc3: return 0
            if pc5 < s_sc5: return 0
            if pc7 < s_sc7: return 0
            
            return 1 # All checks passed: P is non-zero and S divides P.

        ans = 0
        limit = int(self.snum_str[idx]) if tight else 9 # Max digit we can place

        for digit in range(limit + 1):
            new_tight = tight and (digit == limit) # tight constraint for next state
            
            if is_leading and digit == 0:
                # Still placing leading zeros. State mostly unchanged.
                # has_zero flag is for non-leading zeros.
                ans += self._dp(idx + 1, current_sum, pc2, pc3, pc5, pc7, new_tight, True, False)
            else:
                # Prune if sum exceeds max possible (81 for N < 10^9)
                if current_sum + digit > Solution.MAX_SUM_DIGITS: 
                     continue 

                # If digit is 0 (and not a leading zero), then new_has_zero becomes true.
                new_has_zero = has_zero or (digit == 0) 
                
                d_c2, d_c3, d_c5, d_c7 = Solution.d_factors_static[digit]
                
                # Update product's prime factor counts.
                # These counts are only relevant if new_has_zero is False.
                # If new_has_zero is True, product P=0. We pass them along anyway for consistent state.
                new_pc2 = min(Solution.C2_CAP, pc2 + d_c2) 
                new_pc3 = min(Solution.C3_CAP, pc3 + d_c3)
                new_pc5 = min(Solution.C5_CAP, pc5 + d_c5)
                new_pc7 = min(Solution.C7_CAP, pc7 + d_c7)
                
                ans += self._dp(idx + 1, current_sum + digit, \
                              new_pc2, new_pc3, new_pc5, new_pc7, \
                              new_tight, False, new_has_zero)
        
        self.memo[state] = ans
        return ans

    def _solve_N(self, N_val):
        if N_val == 0: return 0 # No positive beautiful numbers up to 0.
        
        self.snum_str = str(N_val)
        self.D = len(self.snum_str) # Number of digits in N_val
        self.memo = {} # Clear memo for this specific N_val calculation.
        
        # Initial call: idx=0, sum=0, all pc_i=0, tight=True, is_leading=True, has_zero=False
        return self._dp(0, 0, 0,0,0,0, True, True, False)

    def beautifulNumbers(self, l, r):
        # Ensure precomputation tables are ready (call once per Solution object or globally)
        self._ensure_precomputation()
        
        count_r = self._solve_N(r)
        count_l_minus_1 = self._solve_N(l - 1)
        
        return count_r - count_l_minus_1
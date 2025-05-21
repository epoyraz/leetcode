class Solution(object):
    # --- Sieve precomputation as static class members ---
    # This code runs once when the class Solution is defined.
    MAX_VAL_S_STATIC = 1000000 
    _spf_table_s = range(MAX_VAL_S_STATIC + 1) # Initialize spf[i] = i

    _sqrt_MAX_VAL_s = int(MAX_VAL_S_STATIC**0.5)
    for i in xrange(2, _sqrt_MAX_VAL_s + 1):
        if _spf_table_s[i] == i: # i is prime
            # Mark multiples of i. Start from i*i.
            for j in xrange(i*i, MAX_VAL_S_STATIC + 1, i):
                if _spf_table_s[j] == j: # If spf[j] is still j, then i is its smallest prime factor
                    _spf_table_s[j] = i
    # --- End of Sieve precomputation ---

    def minOperations(self, nums):
        n = len(nums)
        # infinity is a value larger than any possible operation count (max n ops).
        infinity = n + 1 

        # prev_ops0: min_ops for prefix ending at nums[i-1], if nums[i-1] took its original value.
        # prev_val0: the original value of nums[i-1].
        prev_ops0 = 0
        prev_val0 = 0 # Initial "previous value" before nums[0] is 0. Smallest nums[i] is 1.

        # prev_ops1: min_ops for prefix ending at nums[i-1], if nums[i-1] took its SPF value.
        # prev_val1: the SPF value of nums[i-1].
        prev_ops1 = 0
        prev_val1 = 0

        # Local reference to the static SPF table.
        spf_table_local_ref = Solution._spf_table_s

        for i in xrange(n):
            num_val = nums[i]

            # Case 1: nums[i] keeps its original value (num_val)
            # Cost for current element: 0 operations.
            current_orig_val = num_val
            current_orig_ops = infinity # Initialize with infinity
            
            # Check if num_val is non-decreasing w.r.t. prev_val0
            if num_val >= prev_val0:
                current_orig_ops = min(current_orig_ops, prev_ops0)
            # Check if num_val is non-decreasing w.r.t. prev_val1
            if num_val >= prev_val1:
                current_orig_ops = min(current_orig_ops, prev_ops1)

            # Case 2: nums[i] is transformed to its SPF
            # Cost for current element: 1 operation.
            current_spf_val = infinity # Default if transformation is not possible/applicable
            current_spf_ops = infinity # Initialize with infinity

            # Transformation is possible if num_val is composite and greater than 1.
            # spf_table_local_ref[num_val] will be < num_val if composite.
            # spf_table_local_ref[num_val] will be == num_val if prime.
            if num_val > 1 and spf_table_local_ref[num_val] != num_val:
                val_i_spf = spf_table_local_ref[num_val]
                current_spf_val = val_i_spf
                
                # Check if val_i_spf is non-decreasing w.r.t. prev_val0
                if val_i_spf >= prev_val0:
                    # prev_ops0 + 1 might exceed infinity if prev_ops0 is already infinity.
                    # This is fine as long as infinity + 1 is still treated as "more than any valid count".
                    current_spf_ops = min(current_spf_ops, prev_ops0 + 1)
                # Check if val_i_spf is non-decreasing w.r.t. prev_val1
                if val_i_spf >= prev_val1:
                    current_spf_ops = min(current_spf_ops, prev_ops1 + 1)
            
            # Update 'prev' states for the next iteration
            prev_val0 = current_orig_val
            prev_ops0 = current_orig_ops
            prev_val1 = current_spf_val
            prev_ops1 = current_spf_ops
        
        min_total_ops = min(prev_ops0, prev_ops1)

        if min_total_ops >= infinity: # Use >= just in case infinity + 1 was stored
            return -1
        else:
            return min_total_ops
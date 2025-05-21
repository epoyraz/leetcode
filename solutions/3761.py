import sys

class Solution(object):
    def maxDifference(self, s, k):
        N = len(s)
        C = 5 # Characters '0' through '4'

        # counts[char_code][prefix_len]: count of char_code in s[0...prefix_len-1]
        counts = [[0] * (N + 1) for _ in xrange(C)]
        # parity_masks_P[prefix_len]: parity mask for s[0...prefix_len-1]
        parity_masks_P = [0] * (N + 1) 

        # Base case for empty prefix (length 0): counts are 0, parity_mask is 0.
        # These are already initialized by Python's default list/int creation.

        for i in xrange(N):
            char_code = int(s[i]) # Map '0'->0, '1'->1, ..., '4'->4
            
            # Copy counts from previous prefix length
            for c_idx in xrange(C):
                counts[c_idx][i+1] = counts[c_idx][i]
            
            counts[char_code][i+1] += 1 # Increment count for current character
            
            # Update parity mask for prefix of length i+1
            # P[i+1] = P[i] XOR (1 << char_code_of_s[i])
            parity_masks_P[i+1] = parity_masks_P[i] ^ (1 << char_code)

        max_overall_diff = -N - 1 # Initialize with a value smaller than any possible valid difference
        found_any = False # To track if any valid substring satisfying conditions is found

        for ca_idx in xrange(C):       # Index for character 'a'
            for cb_idx in xrange(C):   # Index for character 'b'
                if ca_idx == cb_idx:
                    continue

                # min_val_for_parity_mask[mask] stores min(counts[ca_idx][j_l] - counts[cb_idx][j_l])
                # for prefixes s[0...j_l-1] (length j_l) having parity 'mask'.
                # Using a list of size 2^C as C is small and fixed.
                min_val_for_parity_mask = [sys.maxint] * (1 << C)

                # j_r: length of prefix s[0...j_r-1]. Substring ends at s[j_r-1].
                # Smallest j_r for a substring of length k is k itself (substring s[0...k-1]).
                for j_r in xrange(k, N + 1):
                    # Current substring is s[j_l_start_idx ... j_r-1].
                    # Its length is (j_r-1) - j_l_start_idx + 1 = j_r - j_l_start_idx.
                    # The prefix corresponding to j_l_start_idx is s[0...j_l_start_idx-1], indexed by j_l_start_idx.
                    # Let j_l be the length of prefix s[0...j_l-1].
                    # Condition: length j_r - j_l >= k  =>  j_l <= j_r - k.
                    
                    # The prefix whose length is j_l_for_update = j_r - k becomes relevant.
                    # This is s[0...(j_r-k)-1].
                    j_l_for_update = j_r - k
                    
                    mask_at_j_l_update = parity_masks_P[j_l_for_update]
                    val_at_j_l_update = counts[ca_idx][j_l_for_update] - counts[cb_idx][j_l_for_update]
                    
                    if val_at_j_l_update < min_val_for_parity_mask[mask_at_j_l_update]:
                        min_val_for_parity_mask[mask_at_j_l_update] = val_at_j_l_update
                    
                    # Query using current P[j_r] and counts for prefix of length j_r
                    current_mask_j_r = parity_masks_P[j_r]
                    
                    # Target parity for P[j_l]_ca, for ca's freq in substring to be odd:
                    # (P[j_r]_ca ^ P[j_l]_ca) == 1  => P[j_l]_ca == (P[j_r]_ca ^ 1)
                    target_parity_P_j_l_ca = ((current_mask_j_r >> ca_idx) & 1) ^ 1
                    
                    # Target parity for P[j_l]_cb, for cb's freq in substring to be even:
                    # (P[j_r]_cb ^ P[j_l]_cb) == 0  => P[j_l]_cb == P[j_r]_cb
                    target_parity_P_j_l_cb = (current_mask_j_r >> cb_idx) & 1 # No ^0 needed

                    current_val_at_j_r = counts[ca_idx][j_r] - counts[cb_idx][j_r]

                    # Iterate over all possible_mask_j_l (0 to 2^C - 1)
                    for possible_mask_j_l in xrange(1 << C):
                        min_val_j_l = min_val_for_parity_mask[possible_mask_j_l]
                        if min_val_j_l == sys.maxint: # No prefix j_l seen with this mask for this (ca,cb) pair
                            continue

                        # Extract parities of ca and cb from possible_mask_j_l
                        parity_P_j_l_ca = (possible_mask_j_l >> ca_idx) & 1
                        parity_P_j_l_cb = (possible_mask_j_l >> cb_idx) & 1

                        if parity_P_j_l_ca == target_parity_P_j_l_ca and \
                           parity_P_j_l_cb == target_parity_P_j_l_cb:
                            
                            # This P[j_l] is a valid candidate for left part of value calculation
                            diff = current_val_at_j_r - min_val_j_l
                            if not found_any or diff > max_overall_diff:
                                max_overall_diff = diff
                            found_any = True # Mark that at least one valid diff was computed
        
        # If no substring satisfied all conditions, max_overall_diff remains its initial -N-1.
        # The problem examples imply that valid negative results (like -1) are possible.
        # The problem constraint "at least one substring has a character with an even frequency 
        # and a character with an odd frequency" might not guarantee this substring also meets length k.
        # So, found_any could theoretically be false. If this can happen, the specific return value
        # for "not found" would be needed from problem spec (e.g. 0, -1, or error).
        # Given typical contest styles, returning the calculated max_overall_diff (even if it's the initial -N-1)
        # is standard unless specified otherwise.
        return max_overall_diff
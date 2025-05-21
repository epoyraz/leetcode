import collections

class Solution(object):
    def longestCommonPrefix(self, words, k):
        n = len(words)
        ans = [0] * n

        if n < k: # Not even enough words initially
            return [0] * n
        
        # Handle the edge case where after removing a word, there are not enough strings
        if n - 1 < k:
            # This means k = n. We need all n-1 strings.
            # If k=n=1, then n-1=0 < k=1. answer[0]=0.
            # If n=0, no, n>=1. words.length >= k, so n >= k.
            # This case occurs if k = n.
            # Then after removing 1 word, we have n-1 words. We need LCP of k=n words. Impossible.
             for i in xrange(n):
                 ans[i] = 0 # Not enough words left.
             if k==0: # LCP of 0 strings is undefined or infinite. If k>=1, this is fine.
                 # Constraints say 1 <= k.
                 pass # ans is already [0]*n
             return ans


        # Trie Node structure (using dictionary for children)
        # {'#count': 0, '#depth': d, '#paths': set(), 'c': child_node, ...}
        # '#count' = number of original words passing through this node
        # '#depth' = depth of node (length of prefix)
        # '#paths' = set of indices of original words passing through this node
        
        trie = {'#count': 0, '#depth': 0, '#paths': set()}

        for i, word in enumerate(words):
            node = trie
            node['#count'] += 1
            node['#paths'].add(i)
            for char_idx, char in enumerate(word):
                if char not in node:
                    node[char] = {'#count': 0, '#depth': char_idx + 1, '#paths': set()}
                node = node[char]
                node['#count'] += 1
                node['#paths'].add(i)
        
        # Calculate L0: max depth of a node u where count[u] >= k+1
        L0 = 0
        
        # Collect nodes for V_k: (depth, PathStrings_set) for nodes u where count[u] = k
        # M_D = list of (depth, frozenset_of_PathStrings)
        M_D = [] 

        queue = collections.deque([trie])
        visited_nodes_for_MD = [] # Store actual node dicts to avoid reparsing

        while queue:
            node = queue.popleft()
            
            count_u = node['#count']
            depth_u = node['#depth']

            if count_u >= k + 1:
                L0 = max(L0, depth_u)
            
            if count_u == k:
                # Store depth and the set of paths (indices of words)
                # PathStrings set must be frozenset to be hashable if used as dict key later
                M_D.append((depth_u, frozenset(node['#paths'])))

            for char_code in "abcdefghijklmnopqrstuvwxyz":
                if char_code in node:
                    queue.append(node[char_code])
        
        for i in xrange(n):
            ans[i] = L0

        # Sort M_D by depth descending. If depths equal, doesn't strictly matter for this logic.
        M_D.sort(key=lambda p: p[0], reverse=True)
        
        # Optimized L1 calculation:
        # For each distinct depth d (descending):
        #   intersect_S_d = intersection of all PathStrings sets for this depth d
        #   For unresolved i: if i is NOT in intersect_S_d, then L1[i] = d.
        
        L1_values = [0] * n # Stores L1(i)
        
        # Group M_D by depth
        depth_to_path_sets = collections.defaultdict(list)
        for depth_val, path_set_val in M_D:
            depth_to_path_sets[depth_val].append(path_set_val)

        sorted_unique_depths = sorted(depth_to_path_sets.keys(), reverse=True)

        unresolved_indices = list(range(n)) # Indices for which L1_values[idx] is not set

        for d_val in sorted_unique_depths:
            if not unresolved_indices:
                break
            
            path_sets_for_d = depth_to_path_sets[d_val]
            
            # Calculate intersection_of_all_S_for_this_d
            # If no sets for this depth (should not happen due to defaultdict construction),
            # treat intersection as empty (so all unresolved_indices get this d_val).
            # This means if path_sets_for_d is empty, any index i is not in intersection.
            
            # Initial intersection: if no sets, all indices qualify (i.e., not in empty intersection).
            # If sets exist, start with the first set.
            # All indices in `range(n)` are candidates if this list is empty.
            # Effectively, if path_sets_for_d is empty, intersection should be an empty set,
            # meaning for any i, i is NOT in the intersection.
            
            current_intersection = set() 
            if path_sets_for_d: # only if list is not empty
                # Initialize with a copy of the first set
                current_intersection = set(path_sets_for_d[0]) 
                for s_idx in xrange(1, len(path_sets_for_d)):
                    current_intersection.intersection_update(path_sets_for_d[s_idx])
            
            next_unresolved_indices = []
            for idx in unresolved_indices:
                # An index `idx` gets this depth `d_val` if there is AT LEAST ONE path_set for `d_val`
                # that does NOT contain `idx`.
                # This is equivalent to: `idx` is NOT IN (intersection of all path_sets for `d_val`).
                if not path_sets_for_d: # No sets of count k at this depth
                    # This case should not occur given how sorted_unique_depths is made
                    next_unresolved_indices.append(idx) # Still unresolved by this (empty) depth
                    continue

                if idx not in current_intersection:
                    L1_values[idx] = d_val
                    # This idx is now resolved for L1
                else:
                    # idx is in ALL path_sets for this depth d_val.
                    # So, d_val is not a candidate for L1_values[idx].
                    # It remains unresolved for a potentially smaller depth.
                    next_unresolved_indices.append(idx)
            
            unresolved_indices = next_unresolved_indices

        for i in xrange(n):
            ans[i] = max(ans[i], L1_values[i])
            
        return ans
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Map each string in list1 to its index
        index_map = {s: i for i, s in enumerate(list1)}
        best_sum = float('inf')
        result = []
        
        # Iterate through list2 and look for common strings
        for j, s in enumerate(list2):
            if s in index_map:
                i = index_map[s]
                idx_sum = i + j
                # Found a smaller index sum: reset result
                if idx_sum < best_sum:
                    best_sum = idx_sum
                    result = [s]
                # Found an equal index sum: append to result
                elif idx_sum == best_sum:
                    result.append(s)
        
        return result

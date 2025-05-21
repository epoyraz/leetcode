class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        
        # Step 1: Find the first index i such that arr[i] > arr[i + 1]
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
        else:
            return arr  # Already smallest permutation
        
        # Step 2: Find the largest j > i such that arr[j] < arr[i]
        # and arr[j] is the largest possible such value (but if duplicates, take leftmost)
        j = n - 1
        while j > i:
            if arr[j] < arr[i]:
                # Move to the left to get the leftmost one if duplicates exist
                while j - 1 > i and arr[j] == arr[j - 1]:
                    j -= 1
                break
            j -= 1

        # Step 3: Swap and return
        arr[i], arr[j] = arr[j], arr[i]
        return arr

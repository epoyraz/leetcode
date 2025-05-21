class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0] * len(nums)
        indexed_nums = list(enumerate(nums))
        
        def merge_sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])
                m, n = len(left), len(right)
                i = j = 0
                sorted_enum = []
                while i < m or j < n:
                    if j == n or (i < m and left[i][1] <= right[j][1]):
                        counts[left[i][0]] += j
                        sorted_enum.append(left[i])
                        i += 1
                    else:
                        sorted_enum.append(right[j])
                        j += 1
                return sorted_enum
            else:
                return enum
        
        merge_sort(indexed_nums)
        return counts

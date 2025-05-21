class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # Helper function to map a number using the provided mapping
        def mapped_value(num):
            # Convert the number to a string and map each digit using the mapping array
            mapped_num = ''.join(str(mapping[int(digit)]) for digit in str(num))
            # Remove leading zeros by converting to integer and back to string
            return int(mapped_num)
        
        # Sort the nums array using a key based on the mapped value of each number
        return sorted(nums, key=lambda num: mapped_value(num))

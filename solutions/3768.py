class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert to list of ints for faster arithmetic
        arr = list(map(int, s))
        # keep collapsing until length is 2
        while len(arr) > 2:
            # each new digit is sum of consecutive pair mod 10
            arr = [(arr[i] + arr[i+1]) % 10 for i in range(len(arr) - 1)]
        # check if the final two are equal
        return arr[0] == arr[1]

class Solution:
    def smallestString(self, s):
        n = len(s)
        arr = list(s)
        
        # skip leading 'a's
        i = 0
        while i < n and arr[i] == 'a':
            i += 1
        
        # if all 'a's, change last 'a' to 'z'
        if i == n:
            arr[-1] = 'z'
        else:
            # decrement until hitting an 'a' or end
            while i < n and arr[i] != 'a':
                arr[i] = chr(ord(arr[i]) - 1)
                i += 1
        
        return ''.join(arr)

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        
        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(start, path):
            # If we've reached the end of the string, we've found a valid partition
            if start == len(s):
                result.append(path[:])
                return
            
            # Try all possible substrings starting from 'start'
            for end in range(start, len(s)):
                # If substring s[start:end+1] is a palindrome, add it to our path
                if is_palindrome(start, end):
                    path.append(s[start:end+1])
                    # Recursively find all palindrome partitions for the rest of the string
                    backtrack(end + 1, path)
                    # Backtrack to try other possibilities
                    path.pop()
        
        backtrack(0, [])
        return result
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(path, index):
            if index == len(digits):
                res.append(path)
                return
            for char in phone[digits[index]]:
                backtrack(path + char, index + 1)
        
        backtrack("", 0)
        return res

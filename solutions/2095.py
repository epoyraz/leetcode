class Solution(object):
    def minSwaps(self, s):
        balance = 0
        max_unbalanced = 0
        for c in s:
            if c == '[':
                balance += 1
            else:  # c == ']'
                balance -= 1
                if balance < 0:
                    # one more ']' than '[' â unbalanced
                    max_unbalanced = max(max_unbalanced, -balance)
        # Each swap fixes two unbalanced brackets
        return (max_unbalanced + 1) // 2

class Solution:
    def minMovesToMakePalindrome(self, s):
        s = list(s)
        i, j = 0, len(s) - 1
        moves = 0

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                left, right = i, j
                while left < j and s[left] != s[j]:
                    left += 1
                while right > i and s[right] != s[i]:
                    right -= 1
                if left != j:
                    while left > i:
                        s[left], s[left - 1] = s[left - 1], s[left]
                        left -= 1
                        moves += 1
                    i += 1
                    j -= 1
                else:
                    while right < j:
                        s[right], s[right + 1] = s[right + 1], s[right]
                        right += 1
                        moves += 1
                    i += 1
                    j -= 1

        return moves

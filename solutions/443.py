class Solution:
    def compress(self, chars):
        write = 0
        left = 0
        
        for right in range(len(chars)):
            if right == len(chars) - 1 or chars[right] != chars[right + 1]:
                chars[write] = chars[right]
                write += 1
                count = right - left + 1
                if count > 1:
                    for c in str(count):
                        chars[write] = c
                        write += 1
                left = right + 1
        
        return write

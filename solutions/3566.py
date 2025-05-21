class Solution(object):
    def stringSequence(self, target):
        """
        :type target: str
        :rtype: List[str]
        """
        result = []
        screen = ""
        for c in target:
            # 1) Press Key 1: append 'a'
            screen += 'a'
            result.append(screen)
            
            # 2) Press Key 2 dist times to shift 'a' â c
            dist = ord(c) - ord('a')  # 0..25
            for _ in range(dist):
                last = screen[-1]
                # increment with wrap 'z' â 'a'
                if last == 'z':
                    nxt = 'a'
                else:
                    nxt = chr(ord(last) + 1)
                screen = screen[:-1] + nxt
                result.append(screen)
        
        return result

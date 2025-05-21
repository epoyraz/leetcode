class Solution(object):
    def interpret(self, command):
        res = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                res.append('G')
                i += 1
            elif command[i:i+2] == '()':
                res.append('o')
                i += 2
            else:
                res.append('al')
                i += 4
        return ''.join(res)

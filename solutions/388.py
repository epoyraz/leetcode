class Solution:
    def lengthLongestPath(self, input):
        max_length = 0
        path_length = {0: 0}
        
        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.lstrip('\t')
            if '.' in name:
                max_length = max(max_length, path_length[depth] + len(name))
            else:
                path_length[depth + 1] = path_length[depth] + len(name) + 1  # +1 for '/'
        
        return max_length

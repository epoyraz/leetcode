class Solution(object):
    def numSimilarGroups(self, strs):
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        def is_similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
            return diff == 2 or diff == 0
        
        n = len(strs)
        for word in strs:
            parent[word] = word
        
        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]):
                    union(strs[i], strs[j])
        
        groups = set()
        for word in strs:
            groups.add(find(word))
        
        return len(groups)

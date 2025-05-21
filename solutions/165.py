class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        max_len = max(len(v1), len(v2))
        
        for i in range(max_len):
            num1 = v1[i] if i < len(v1) else 0
            num2 = v2[i] if i < len(v2) else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        
        return 0

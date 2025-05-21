class Solution(object):
    def containsPattern(self, arr, m, k):
        n = len(arr)
        for i in range(n - m * k + 1):
            pattern = arr[i:i+m]
            count = 1
            for j in range(i + m, n, m):
                if arr[j:j+m] == pattern:
                    count += 1
                    if count >= k:
                        return True
                else:
                    break
        return False
